import datetime
from pathlib import Path
from pyboy.pyboy import *
from gym.wrappers import FrameStack, NormalizeObservation
from AISettings.AISettingsInterface import AISettingsInterface
from AISettings.MarioAISettings import MarioAI
from AISettings.KirbyAISettings import KirbyAI
from MetricLogger import MetricLogger
from agent import AIPlayer
from wrappers import SkipFrame, ResizeObservation
import sys
from CustomPyBoyGym import CustomPyBoyGym
from functions import alphanum_key

# Variables
episodes = 40000
observation_types = ["raw", "tiles", "compressed", "minimal"]
observation_type = observation_types[1]
action_types = ["press", "toggle", "all"]
action_type = action_types[0]
gameDimentions = (20, 16)
frameStack = 4
quiet = False
train = False
playtest = False

# Set up the path to your Mega Man 2 ROM
rom_path = "/Users/benjaminhetrick/ROMS/mm2.gb"

# Check if the game ROM exists
if not Path(rom_path).exists():
    print("Game ROM not found at", rom_path)
    sys.exit(1)

# Initialize PyBoy with the game ROM
pyboy = PyBoy(rom_path)

# Your existing setup code for AI training, evaluation, etc.

# Choose mode (simplified for demonstration)
modes = ["Evaluate (HEADLESS)", "Evaluate (UI)", "Train (HEADLESS)", "Train (UI)", "Playtest (UI)"]
for cnt, modeName in enumerate(modes, 1):
    sys.stdout.write("[%d] %s\n\r" % (cnt, modeName))

choice = int(input("Select mode[1-%s]: " % cnt)) - 1
mode = modes[choice]

# Initialize the environment based on the selected mode
# Add your logic to handle different modes (HEADLESS/UI, Train/Evaluate/Playtest)

# Example for starting the game in a specific mode
if "HEADLESS" in mode:
    pyboy.set_emulation_speed(0)  # Run as fast as possible
else:
    pyboy.set_emulation_speed(1)  # Normal speed

# Example for training the AI
if "Train" in mode:
    # Your training logic here
    pass

# Example for evaluation
if "Evaluate" in mode:
    # Your evaluation logic here
    pass

# Example for playtesting
if "Playtest" in mode:
    # Your playtesting logic here
    pass