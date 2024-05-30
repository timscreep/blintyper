import os
import subprocess

from datetime import datetime, time
from random import choice

from PIL import Image
from pystray import Icon, Menu
from pystray import MenuItem as item
from shutil import which


# Set the paths to the required files
milashka_file_path = "milashka.txt"
texts_file_path = "texts.txt"
tray_image_path = "blin.png"


def time_intervals(current_time, line):
    if (current_time >= time(20, 0)) or (current_time < time(4, 0)):
        line = f"доброй ночи, {line} ❤️"
    elif current_time >= time(12, 0):
        line = f"как дела, {line}?❤️"
    elif current_time >= time(4, 0):
        line = f"доброе утро, {line} ❤️"
    return line


def type_text(text):
    if (os.environ.get("WAYLAND_DISPLAY") and which("wtype")):
        subprocess.run(f"wtype {text} -P Return -p Return", shell = True)


def make_type_text_action(text):
    def action(icon):
        return type_text(text)
    return action


def love():
    current_time = datetime.now().time()
    with open(milashka_file_path, 'r') as milashka_file:
        lines = milashka_file.readlines()
    line = choice(lines)[:-1]
    # Define the time intervals and phrases for all of them
    text = (time_intervals(current_time, line))
    type_text(text)


# Define the texts and actions for the context menu
with open(texts_file_path, 'r') as texts_file:
    texts = [text[:-1] for text in texts_file.readlines()]

# Create the menu items
menu_items = [item(text, make_type_text_action(text)) for text in texts]
menu_items.append(item("love", love))
menu = Menu(*menu_items)

# Create the system tray icon
image = Image.open(tray_image_path)
icon = Icon("blin_icon", image, "Blin Typer", menu)

# Run the icon
icon.run()
