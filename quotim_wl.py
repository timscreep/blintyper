import os
import subprocess


from PIL import Image
from pystray import Icon, Menu
from pystray import MenuItem as item
from shutil import which
import keyboard
from Plugins import Love, Dr, NewYear
# Set the paths to the required files
texts_file_path = "texts.txt"
tray_image_path = "blin.png"



def type_text(text):
    if (os.environ.get("WAYLAND_DISPLAY") and which("wtype")):
       subprocess.run(f"wtype {text} -P Return -p Return", shell = True)


def make_type_text_action(text):
    def action(icon):
        return type_text(text)
    return action

def love():
    type_text(Love.love())
def НовыйГод():
    type_text(NewYear.ОсталосьДоНГ())
def ДеньРождения():
    type_text(Dr.ОсталосьДоДр())
# Define the texts and actions for the context menu
with open(texts_file_path, 'r') as texts_file:
    texts = [text[:-1] for text in texts_file.readlines()]

# Create the menu items
menu_items = [item(text, make_type_text_action(text)) for text in texts]
menu_items.append(item("love", love))
menu_items.append(item("До НГ", НовыйГод))
menu_items.append(item("До ДР Стаси", ДеньРождения))

menu = Menu(*menu_items)

# Create the system tray icon
image = Image.open(tray_image_path)
icon = Icon("blin_icon", image, "Blin Typer", menu)

# Run the icon
icon.run()
