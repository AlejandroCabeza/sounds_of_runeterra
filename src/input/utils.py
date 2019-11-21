# Python Imports
from msvcrt import getch
# Third-Party Imports
# Project Imports
from input.config import KEY_CODE_ENTER, KEY_CODE_SPACE


def get_keyboard_input_as_integer():
    return ord(getch())


async def _parse_keyboard_inputs(key_code: int):
    if key_code is KEY_CODE_ENTER:
        print("ENTER")
    elif key_code is KEY_CODE_SPACE:
        print("SPACE")
