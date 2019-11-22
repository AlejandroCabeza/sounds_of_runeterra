# Python Imports
# Third-Party Imports
from screeninfo import get_monitors
# Project Imports


# Due to sanity reasons we assume Legends of Runeterra is running in the main monitor at a fullscreen resolution
# Because we don't know in what monitor it's running
MONITOR = get_monitors()[0]
SCREEN_SIZE: (int, int) = (MONITOR.width, MONITOR.height)
