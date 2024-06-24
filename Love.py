from datetime import datetime, time
from random import choice


def time_intervals(current_time, line):
    if (current_time >= time(20, 0)) or (current_time < time(4, 0)):
        line = f"доброй ночи, {line} ❤️"
    elif current_time >= time(12, 0):
        line = f"как дела, {line}? ❤️"
    elif current_time >= time(4, 0):
        line = f"доброе утро, {line} ❤️"
    return line


def love():
    current_time = datetime.now().time()
    with open("milashka.txt", 'r') as milashka_file:
        lines = milashka_file.readlines()
    line = choice(lines)[:-1]
    # Define the time intervals and phrases for all of them
    text = (time_intervals(current_time, line))
    return text

