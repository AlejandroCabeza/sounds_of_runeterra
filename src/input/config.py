# Python Imports
# Third-Party Imports
from screeninfo import get_monitors
# Project Imports

# We are supposing Legends of Runeterra is running in the main monitor at a fullscreen resolution
MONITOR = get_monitors()[0]
SCREEN_SIZE: (int, int) = (MONITOR.width, MONITOR.height)
