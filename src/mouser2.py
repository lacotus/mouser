#!/user/bin/env python3

from pynput import keyboard
import mouse
import subprocess

active_keys = ['', '']

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

distance = 20
duration = 0.01

def move_mouse():
    if active_keys == [up, '']:
        x = 0
        y = -1

    elif active_keys == [down, '']:
        x = 0
        y = 1

    elif active_keys == ['', left]:
        x = -1
        y = 0

    elif active_keys == ['', right]:
        x = 1
        y = 0

    elif active_keys == [up, left]:
        x = -1
        y = -1

    elif active_keys == [up, right]:
        x = 1
        y = -1

    elif active_keys == [down, left]:
        x = -1
        y = 1

    elif active_keys == [down, right]:
        x = 1
        y = 1
       
    if active_keys != ['', '']:
        mouse.move((distance * x), (distance * y), absolute=False, duration=duration)
        

def set_active_keys(key): 
    if (key.char == up):
        active_keys[0] = up

    elif (key.char == down):
        active_keys[0] = down

    elif (key.char == left):
        active_keys[1] = left

    elif (key.char == right):
        active_keys[1] = right
    
def remove_active_keys(key): 
    if (key.char == up):
        active_keys[0] = ''

    elif (key.char == down):
        active_keys[0] = ''

    elif (key.char == left):
        active_keys[1] = ''

    elif (key.char == right):
        active_keys[1] = ''

    elif (key.char == stop_key):
        exit()

def handle_click(key):
    if key.char == click_left:
        subprocess.call(["xdotool", "click", "1"])
    
    elif key.char == click_middle:
        subprocess.call(["xdotool", "click", "2"])

    elif key.char == click_right:
        subprocess.call(["xdotool", "click", "3"])

    elif key.char == scroll_up:
        subprocess.call(["xdotool", "click", "4"])

    elif key.char == scroll_down:
        subprocess.call(["xdotool", "click", "5"])

def on_press(key):
    try:
        # To console
        print('alpha key {0} pressed'.format(key.char))

        # Set active_keys
        set_active_keys(key)

        # Move the mouse
        move_mouse()

        # Handle all clicking / non-moving keys
        handle_click(key)

        print("Active keys: " + ' '.join(active_keys))
    except Exception as e:
        print('special key {0} pressed'.format(key))
        print(e)

def on_release(key):
    print('{0} released'.format(key))
    try:
        # Removes the keys from active_keys as they are being released
        remove_active_keys(key)

        print("Active keys: " + ' '.join(active_keys))
    except Exception as e:
        print(e)



with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True) as listener:
    listener.join()


