#!/usr/bin/env python3

import mouse
import keyboard

while True:

    reg_speed = 75

    # First 'if', triggered when key is pressed
    if (keyboard.read_key()):
        
        # Second 'if', reads what is being pressed

        # Organized into two sections: Multis (with subsections: e, s, and d) and Singles
        # Multis define more than one key press, Singles define singles

        # Section 1 - Speed control
        if (keyboard.is_pressed('space')):
            print("space is pressed")
            reg_speed = 150
        elif (keyboard.is_pressed('shift')):
            print("shift is pressed")
            reg_speed = 10

        # Section 2 - Multis
        # Subsection 1.1 - 'e', defines 'es (se)', 'ed (de)', and 'ef (fe)' relationships
        if (keyboard.is_pressed('e') and keyboard.is_pressed('s')):
            print("You are pressing 'es' (or 'se')")
            mouse.move(-reg_speed, -reg_speed, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('d')):
            print("You are pressing 'ed' (or 'de')")
            mouse.move(0, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('f')):
            print("You are pressing 'ef' (or 'fe')")
            mouse.move(reg_speed, -reg_speed, absolute=False, duration=0.2)
            continue

        # Subsection 1.2 - 's', defines 'sd (ds)' and 'sf (fs)' relationships
        elif (keyboard.is_pressed('s') and keyboard.is_pressed('d')):
            print("You are pressing 'sd' (or 'ds')")
            mouse.move(-reg_speed, reg_speed, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('s') and keyboard.is_pressed('f')):
            print("You are pressing 'sf' (or 'fs')")
            mouse.move(0, 0, absolute=False, duration=0.2)
            continue

        # Subsection 1.3 - 'd', defines 'df (fd)' relationship
        elif (keyboard.is_pressed('d') and keyboard.is_pressed('f')):
            print("You are pressing 'df' (or 'fd')")
            mouse.move(reg_speed, reg_speed, absolute=False, duration=0.2)
            continue
        
        # Section 3 - Singles
        elif (keyboard.is_pressed('e')):
            print("You are pressing 'e'")
            mouse.move(0, -reg_speed, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('s')):
            print("You are pressing 's'")
            mouse.move(-reg_speed, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('d')):
            print("You are pressing 'd'")
            mouse.move(0, reg_speed, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('f')):
            print("You are pressing 'f'")
            mouse.move(reg_speed, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('j')):
            print("You are pressing 'j'")
            mouse.press(button='left')
            mouse.release(button='left')
            continue

        elif (keyboard.is_pressed(';')):
            break
