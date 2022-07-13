#!/usr/bin/env python3

import getpass
import subprocess
import mouse
import keyboard
from pynput import keyboard as kb

up = 'e'
down = 'd'
left = 's'
right = 'f'

speed_turbo = 'space'
speed_slow = 'shift'

click_left = 'j'
click_middle = 'k'
click_right = 'l'

scroll_up = 'u'
scroll_down = 'n'

stop_key = ';'

password_passed = False

def on_press(key):
    print(key + "was pressed")

def get_password():
    sudo_password = getpass.getpass(prompt='sudo password: ')
    p = subprocess.Popen(['sudo', '-S', 'ls'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    try:
        out, err = p.communicate(input=(sudo_password+'\n').encode(),timeout=5)

    except subprocess.TimeoutExpired:
        p.kill()

    return sudo_password

def mouse_up():
    mouse.move(0, -distance, absolute=False, duration=duration)


while True:

    
    distance = 10
    duration = 0.0000002

    # First 'if', triggered when key is pressed
    if (keyboard.read_key()):
       
        # Second 'if', reads what is being pressed

        # Organized into two sections: Multis (with subsections: e, s, and d) and Singles
        # Multis define more than one key press, Singles define singles

        # Section 1 - Speed control
        if (keyboard.is_pressed(speed_turbo)):
            print("speed_turbo was pressed")
            distance = 25
        elif (keyboard.is_pressed(speed_slow)):
            print("speed_slow was pressed")
            distance = 5

        # Section 2 - Multis
        # Subsection 1.1 - 'e', defines 'es (se)', 'ed (de)', and 'ef (fe)' relationships
        if (keyboard.is_pressed(up) and keyboard.is_pressed(left)):
            print("You are pressing up and left")
            mouse.move(-distance, -distance, absolute=False, duration=duration)
            continue

        elif (keyboard.is_pressed(up) and keyboard.is_pressed(down)):
            print("You are pressing up and down")
            mouse.move(0, 0, absolute=False, duration=duration)
            continue

        elif (keyboard.is_pressed(up) and keyboard.is_pressed(right)):
            print("You are pressing up and right")
            mouse.move(distance, -distance, absolute=False, duration=duration)
            continue

        # Subsection 1.2 - 's', defines 'sd (ds)' and 'sf (fs)' relationships
        elif (keyboard.is_pressed(left) and keyboard.is_pressed(down)):
            print("You are pressing left and down")
            mouse.move(-distance, distance, absolute=False, duration=duration)
            continue

        elif (keyboard.is_pressed(left) and keyboard.is_pressed(right)):
            print("You are pressing left and right")
            mouse.move(0, 0, absolute=False, duration=duration)
            continue

        # Subsection 1.3 - 'd', defines 'df (fd)' relationship
        elif (keyboard.is_pressed(down) and keyboard.is_pressed(right)):
            print("You are pressing right and down")
            mouse.move(distance, distance, absolute=False, duration=duration)
            continue
        
        # Section 3 - Singles
        elif (keyboard.is_pressed(up)):
            print("You are pressing up")
            mouse_up()
            continue

        elif (keyboard.is_pressed(left)):
            print("You are pressing left")
            mouse.move(-distance, 0, absolute=False, duration=duration)
            continue

        elif (keyboard.is_pressed(down)):
            print("You are pressing down")
            mouse.move(0, distance, absolute=False, duration=duration)
            continue

        elif (keyboard.is_pressed(right)):
            print("You are pressing right")
            mouse.move(distance, 0, absolute=False, duration=duration)
            continue

        # xdotool keys -> 1 - Left click, 2 - Middle click, 3 - Right click, 4 - Scroll up, 5 - Scroll down
        elif (keyboard.is_pressed('j')):
            print("You are pressing 'j'")
            subprocess.call(["xdotool", "click", "1"])
            continue

        elif (keyboard.is_pressed('k')):
            print("You are pressing 'k'")
            subprocess.call(["xdotool", "click", "2"])
            continue

        elif (keyboard.is_pressed('l')):
            print("You are pressing 'l'")
            subprocess.call(["xdotool", "click", "3"])
            continue

        elif (keyboard.is_pressed('u')):
            print("You are pressing 'u'")
            subprocess.call(["xdotool", "click", "4"])
            continue

        elif (keyboard.is_pressed('n')):
            print("You are pressing 'n'")
            subprocess.call(["xdotool", "click", "5"])
            continue

        elif (keyboard.is_pressed(';')):
            break
