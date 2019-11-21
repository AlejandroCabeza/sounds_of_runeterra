# Python Imports
import asyncio
# Third-Party Imports
from pynput import keyboard
from pynput.keyboard import Key
from pynput.mouse import Controller
# Project Imports
from input.utils import transform_mouse_position_to_bottom_left_coordinate_axis


class InputManager:

    def __init__(self, event_loop, app):
        self.lock = asyncio.locks.Lock()
        self.is_running: bool = False
        self.flag_stop: bool = False
        self.queue: asyncio.Queue = asyncio.Queue(1)
        self.mouse = Controller()
        self.keyboard_listener = keyboard.Listener(on_press=self._parse_keyboard_press)

    def start_keyboard_listener(self):
        self.keyboard_listener.start()

    def get_mouse_position(self):
        top_left_mouse_position = self.mouse.position
        return transform_mouse_position_to_bottom_left_coordinate_axis(top_left_mouse_position)

    async def stop(self):
        async with self.lock:
            self.flag_stop = True
            self.keyboard_listener.stop()

    def _parse_keyboard_press(self, key_code: Key):
        callbacks = {
            Key.enter: lambda *args, **kwargs: print("ENTER"),
            Key.space: self.output_card_hovered_by_mouse  # lambda *args, **kwargs: print("SPACE")
        }
        f = callbacks.get(key_code, lambda *args, **kwargs: print("Unrecognized key"))
        f()

    def output_card_hovered_by_mouse(self):
        mouse_position = self.get_mouse_position()
        card_code = self.get_card_hovered_by_mouse(mouse_position)
        print(card_code)

    def get_card_hovered_by_mouse(self, mouse_position):
        print(mouse_position)


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
