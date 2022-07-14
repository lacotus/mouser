#!/user/bin/env python3

from pynput import keyboard
import mouse
import subprocess

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
duration = 0.1

def move_mouse(x, y):
    mouse.move(x, y, absolute=False, duration=duration)

def on_press(key):
    try:
        print('alpha key {0} pressed'.format(key.char))
        if (key.char == up):
            move_mouse(0, -distance)
    except:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
