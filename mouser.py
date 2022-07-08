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
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('d')):
            print("You are pressing 'ed' (or 'de')")
            continue

        elif (keyboard.is_pressed('e') and keyboard.is_pressed('f')):
            print("You are pressing 'ef' (or 'fe')")
            continue

        # Subsection 1.2 - 's', defines 'sd (ds)' and 'sf (fs)' relationships
        elif (keyboard.is_pressed('s') and keyboard.is_pressed('d')):
            print("You are pressing 'sd' (or 'ds')")
            continue

        elif (keyboard.is_pressed('s') and keyboard.is_pressed('f')):
            print("You are pressing 'sf' (or 'fs')")
            continue

        # Subsection 1.3 - 'd', defines 'df (fd)' relationship
        elif (keyboard.is_pressed('d') and keyboard.is_pressed('f')):
            print("You are pressing 'df' (or 'fd')")
            continue
        
        # Section 2 - Singles
        elif (keyboard.is_pressed('e')):
            print("You are pressing 'e'")
            continue

        elif (keyboard.is_pressed('s')):
            print("You are pressing 's'")
            continue

        elif (keyboard.is_pressed('d')):
            print("You are pressing 'd'")
            continue

        elif (keyboard.is_pressed('f')):
            print("You are pressing 'f'")
            continue
