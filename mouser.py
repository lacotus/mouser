#!/usr/bin/env python3

import mouse
import keyboard
import pygame

while True:

    # First 'if', triggered when key is pressed
    if (keyboard.read_key()):
        
        # Second 'if', reads what is being pressed

        # Organized into two sections: Multis (with subsections: e, s, and d) and Singles
        # Multis define more than one key press, Singles define singles

        # Section 1 - Multis
        # Subsection 1.1 - 'e', defines 'es (se)', 'ed (de)', and 'ef (fe)' relationships
        if (keyboard.is_pressed('e') and keyboard.is_pressed('s')):
            print("You are pressing 'es' (or 'se')")
            mouse.move(-20, -20, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('d')):
            print("You are pressing 'ed' (or 'de')")
            mouse.move(0, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('f')):
            print("You are pressing 'ef' (or 'fe')")
            mouse.move(20, -20, absolute=False, duration=0.2)
            continue

        # Subsection 1.2 - 's', defines 'sd (ds)' and 'sf (fs)' relationships
        elif (keyboard.is_pressed('s') and keyboard.is_pressed('d')):
            print("You are pressing 'sd' (or 'ds')")
            mouse.move(-20, 20, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('s') and keyboard.is_pressed('f')):
            print("You are pressing 'sf' (or 'fs')")
            mouse.move(0, 0, absolute=False, duration=0.2)
            continue

        # Subsection 1.3 - 'd', defines 'df (fd)' relationship
        elif (keyboard.is_pressed('d') and keyboard.is_pressed('f')):
            print("You are pressing 'df' (or 'fd')")
            mouse.move(20, 20, absolute=False, duration=0.2)
            continue
        
        # Section 2 - Singles
        elif (keyboard.is_pressed('e')):
            print("You are pressing 'e'")
            mouse.move(0, -20, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('s')):
            print("You are pressing 's'")
            mouse.move(-20, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('d')):
            print("You are pressing 'd'")
            mouse.move(0, 20, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed('f')):
            print("You are pressing 'f'")
            mouse.move(20, 0, absolute=False, duration=0.2)
            continue

        elif (keyboard.is_pressed(';')):
            break
