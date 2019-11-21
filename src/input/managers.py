# Python Imports
import asyncio
# Third-Party Imports
# Project Imports
from input.config import KEY_CODE_ENTER, KEY_CODE_SPACE
from input.utils import get_keyboard_input_as_integer, _parse_keyboard_inputs


class InputManager:

    def __init__(self):
        self.lock = asyncio.locks.Lock()
        self.is_running: bool = False
        self.flag_stop: bool = False
        self.queue: asyncio.Queue = asyncio.Queue(1)
        asyncio.get_event_loop().run_in_executor(None, self._listen_keyboard)

    def _listen_keyboard(self):
        while not self.flag_stop:
            if self.queue.empty():
                keyboard_input: int = get_keyboard_input_as_integer()
                if keyboard_input in (KEY_CODE_ENTER, KEY_CODE_SPACE):
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

    async def stop(self):
        async with self.lock:
            self.flag_stop = True


if __name__ == '__main__':
    asd = InputManager()
    asyncio.get_event_loop().run_until_complete(asyncio.gather(
        asd.read_keyboard_inputs()
    ))
