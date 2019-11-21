# Python Imports
import asyncio
# Third-Party Imports
from pynput.mouse import Controller
# Project Imports
from input.config import Key
from input.utils import get_keyboard_input_as_integer, _parse_keyboard_inputs


class InputManager:
    def __init__(self, event_loop):
        self.lock = asyncio.locks.Lock()
        self.is_running: bool = False
        self.flag_stop: bool = False
        self.queue: asyncio.Queue = asyncio.Queue(1)
        self.mouse = Controller()
        event_loop.run_in_executor(None, self._listen_keyboard)

    def _listen_keyboard(self):
        while not self.flag_stop:
            if self.queue.empty():
                keyboard_input: Key = Key(get_keyboard_input_as_integer())
                if keyboard_input in (Key.ENTER, Key.SPACE):
                    self.queue.put_nowait(keyboard_input)

    async def read_keyboard_inputs(self):
        async with self.lock:
            assert not self.is_running
            self.is_running = True
        while not self.flag_stop:
            async with self.lock:
                if self.queue.full():
                    key_code = await self.queue.get()
                    await _parse_keyboard_inputs(key_code)
            await asyncio.sleep(1)

    async def get_keyboard_input(self):
        async with self.lock:
            if self.queue.full():
                return await self.queue.get()

    async def get_mouse_position(self):
        return self.mouse.position

    async def stop(self):
        async with self.lock:
            self.flag_stop = True


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    input_manager = InputManager(asyncio.get_event_loop())

    async def t1():
        while True:
            mouse_pos = await input_manager.get_mouse_position()
            print(mouse_pos)
            await asyncio.sleep(1)

    event_loop.run_until_complete(asyncio.gather(
        input_manager.read_keyboard_inputs(),
        t1()
    ))
