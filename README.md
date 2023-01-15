# MapleStory Bot 🐱‍💻

This repository contains a Python script that uses the pyautogui library to play the game MapleStory.  
It utilizes the on-screen keyboard of the user's computer (by using the OpenCV library to recognize the keyboard) to move the player in the game.  

## Why? 🤷
It's important to note that MapleStory, like many online games, has anti-cheat measures in place to detect and prevent the use of automated tools, such as virtual keyboard presses, to play the game. The use of such tools is a violation of the game's terms of service and can result in account suspension or ban. It's recommended to use this script only for educational or testing purposes and not for actual gameplay.

## Getting Started 🚀
### Prerequisites 📋
* Python 3.x
* virtualenv
* Pillow
* PyAutoGUI
* opencv-python

### Installing 🔧
1. Windows:
* Create a new virtual environment with the command `virtualenv env`
* Activate the virtual environment with the command `env\Scripts\activate`
* Install the necessary packages with the command `pip install -r requirements.txt`

2. Linux:
* Create a new virtual environment with the command   `python3 -m venv env`
* Activate the virtual environment with the command   `source env/bin/activate`
* Install the necessary packages with the command   `pip install -r requirements.txt`

### Usage 🔨
1. Before activating the script, take a screenshot of the on-screen keyboard of your computer and name it keyboard.png.
2. Adjust the keys' coordinates in the Keys.py file to match the keys on your on-screen keyboard.
3. Open cmd or terminal using administator\sudo permissions
3. Run `py tests.py` script to check if the keys have been located properly.
4. Run `py main.py` script to activate the bot.

Note: The script is fitted to a specific player and you may need to adjust the code to match the keys of your own player and the layout of your on-screen keyboard.
