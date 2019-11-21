# Python Imports
from msvcrt import getch
# Third-Party Imports
# Project Imports
from input.config import Key


def get_keyboard_input_as_integer():
    key_code = ord(getch())
    try:
        return Key(key_code)
    except ValueError:
        return None


async def _parse_keyboard_inputs(key_code: Key):
    callbacks = {
        Key.ENTER : lambda *args, **kwargs: print("ENTER"),
        Key.SPACE: lambda *args, **kwargs: print("SPACE")
    }
    f = callbacks.get(key_code, lambda *args, **kwargs: print("Unrecognized key"))
    f()
