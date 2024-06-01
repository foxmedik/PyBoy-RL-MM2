# Introduction
This is a fork of the Pyboy-RL project, specifically focused on completing the Game Boy game Mega Man 2. 



Report: [report](https://github.com/lixado/PyBoy-RL/raw/main/README/report.pdf)



# Requirements
- Python3.7 on Windows
- Python3+ on Linux
- PyBoy (https://github.com/Baekalfen/PyBoy)
- SDL2
    - Ubuntu: __`sudo apt install libsdl2-dev`__
    - Fedora: __`sudo dnf install SDL2-devel`__
    - macOS: __`brew install sdl2`__
    - Windows: PyBoy guide https://github.com/Baekalfen/PyBoy/wiki/Installation#windows-10-64-bit Download link https://www.libsdl.org/download-2.0.php
- For package requirements see requirements.txt
- GameBoy ROM files foe Mega Man 2(place this in /games) 
  - Filename must be "mm2.gb"

# Run with Python
To run from source, first install dependencies:
- __`pip3 install -r requirements.txt`__

Then, run:
- __`python3 main.py`__

# Docker
Build command: __`docker build --tag pyboy-rl .`__ 

Once inside the image run __`python3 main.py`__ to start the program. The docker container only supports headless mode, and the game emulator ui will not show up.

# Based on
DDQN - https://arxiv.org/abs/1509.06461

PyTorch RL Super Mario Bros Example - https://pytorch.org/tutorials/intermediate/mario_rl_tutorial.html
