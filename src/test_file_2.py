#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    try:
        print("{0} was pressed".format(key, char))
    except:
        print("special key pressed")
