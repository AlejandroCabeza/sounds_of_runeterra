# Python Imports
import asyncio
from collections import defaultdict
# Third-Party Imports
from pynput import keyboard, mouse
from pynput.keyboard import Key
# Project Imports


class InputManager:

    def __init__(self, asynchronous_event_loop):
        self.event_loop: asyncio.AbstractEventLoop = asynchronous_event_loop
        self.lock = asyncio.locks.Lock()
        self.is_running = False
        self.mouse_listener = mouse.Listener(on_move=self._handle_mouse_move)
        self.keyboard_listener = keyboard.Listener(on_press=self._handle_keyboard_press)
        self._key_subscribed = defaultdict(dict)
        self._mouse_subscribed = {}
        self.mouse_controller = mouse.Controller()

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.is_running = True

    def get_mouse_pos(self):
        return self.mouse_controller.position

    async def key_subscribe(self, key: Key, call_back):
        async with self.lock:
            self._key_subscribed[key][call_back] = call_back

    async def key_unsubscribe(self, key: Key, call_back):
        async with self.lock:
            self._key_subscribed[key].pop(call_back)

    async def mouse_subscribe(self, call_back):
        async with self.lock:
            self._mouse_subscribed[call_back] = call_back

    async def mouse_unsubscribe(self, call_back):
        async with self.lock:
            self._mouse_subscribed.pop(call_back)

    async def stop(self):
        async with self.lock:
            if self.is_running:
                self.keyboard_listener.stop()
                self.mouse_listener.stop()

    def _handle_keyboard_press(self, key: Key):
        async def handle_key(_key: Key, subscribers):
            async with self.lock:
                for subscriber in subscribers:
                    asyncio.run_coroutine_threadsafe(subscriber(_key), self.event_loop)
        asyncio.run_coroutine_threadsafe(handle_key(key, self._key_subscribed[key].values()), self.event_loop)

    def _handle_mouse_move(self, x, y):
        async def handle_key(_x, _y, subscribers):
            async with self.lock:
                for subscriber in subscribers:
                    asyncio.run_coroutine_threadsafe(subscriber(_x, _y), self.event_loop)
        asyncio.run_coroutine_threadsafe(handle_key(x, y, self._mouse_subscribed), self.event_loop)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    input_manager = InputManager(event_loop)
    input_manager.start()

    async def print_it(*args):
        print(*(str(val) for val in args))

    async def main():
        await asyncio.sleep(10)
        await input_manager.stop()

    async def t1():
        await input_manager.key_subscribe(Key.space, print_it)
        await input_manager.key_subscribe(Key.enter, print_it)
        await input_manager.mouse_subscribe(print_it)
        await asyncio.sleep(5)
        await input_manager.key_unsubscribe(Key.space, print_it)
        await input_manager.key_unsubscribe(Key.enter, print_it)
        await input_manager.mouse_unsubscribe(print_it)

    event_loop.run_until_complete(asyncio.gather(
        t1(),
        main(),
    ))
