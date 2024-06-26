import os
import subprocess


from time import sleep
from datetime import datetime, time
from random import choice

from PIL import Image
from pystray import Icon, Menu
from pystray import MenuItem as item
from shutil import which

import pyperclip
from keyboard import press_and_release


# Set the paths to the required files
milashka_file_path = "C:\\Program Files\\blintyper-main\\milashka.txt"
texts_file_path = "C:\\Program Files\\blintyper-main\\texts.txt"
tray_image_path = "C:\\Program Files\\blintyper-main\\blin.png"


def time_intervals(current_time, line):
    if (current_time >= time(20, 0)) or (current_time < time(4, 0)):
        line = f"доброй ночи, {line} ❤️"
    elif current_time >= time(12, 0):
        line = f"как дела, {line}? ❤️"
    elif current_time >= time(4, 0):
        line = f"доброе утро, {line} ❤️"
    return line




def paste(text: str):    
    pyperclip.copy(text)
    press_and_release('ctrl + v')

def type_text(text):
    press_and_release('alt + tab')
    interval = 0.08
    buffer = pyperclip.paste()
    sleep(interval)
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)
    

def make_type_text_action(text):
    def action(icon):
        return type_text(text)
    return action


def love():
    current_time = datetime.now().time()
    with open(milashka_file_path, 'r', encoding='utf8') as milashka_file:
        lines = milashka_file.readlines()
    line = choice(lines)[:-1]
    # Define the time intervals and phrases for all of them
    text = (time_intervals(current_time, line))
    type_text(text)


# Define the texts and actions for the context menu
with open(texts_file_path, 'r', encoding='utf8') as texts_file:
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
