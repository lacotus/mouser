#!/user/bin/env python3

from pynput import keyboard
import mouse
import subprocess
import threading

no_key_pressed = True

movement_keys = ['', ''] # spot 0 represents up/down while spot 1 represents left / right. captures movement.
active_control = '' # for reading which control is active (probably used mostly for click_left and dragging)

# controls: 0 - up, 1 - down, 2 - left, 3 - right, 4 - speed_turbo, 5 - speed_slow, 6 - click_left, 7 - click_middle,
#   8 - click_right, 9 - scroll_up, 10 - scroll_down, 11 - stop_key
controls = ['e', 'd', 's', 'f', 'space', 'shift', 'j', 'k', 'l', 'u', 'n', ';']


up = controls[0]
down = controls[1]
left = controls[2]
right = controls[3]

speed_turbo = controls[4]
speed_slow = controls[5]

click_left = controls[6]
click_middle = controls[7]
click_right = controls[8]

scroll_up = controls[9]
scroll_down = controls[10]

stop_key = controls[11]

distance = 20
duration = 0.035

def move_mouse():
    while True:
        if movement_keys == [up, '']:
            x = 0
            y = -1

        elif movement_keys == [down, '']:
            x = 0
            y = 1

        elif movement_keys == ['', left]:
            x = -1
            y = 0

        elif movement_keys == ['', right]:
            x = 1
            y = 0

        elif movement_keys == [up, left]:
            x = -1
            y = -1

        elif movement_keys == [up, right]:
            x = 1
            y = -1

        elif movement_keys == [down, left]:
            x = -1
            y = 1

        elif movement_keys == [down, right]:
            x = 1
            y = 1

        elif movement_keys == ['', '']:
            x = 0
            y = 0
        

        mouse.move((distance * x), (distance * y), absolute=False, duration=duration)


def manage_movement_keys(called_from, key):
    
    # condition for catching if we're adding or removing
    if called_from == 'set':
        
        # secion: adding
        # condition that reads the key to find out what to add where
        if key.char == up:
            movement_keys[0] = up
        
        elif key.char == down:
            movement_keys[0] = down

        elif key.char == left:
            movement_keys[1] = left

        elif key.char == right:
            movement_keys[1] = right
        else:
            print('Invalid character when adding to movement_keys')
            exit()

    elif called_from == 'remove':

        # section: removing
        # condition that reads the key to find out what to remove from where
        if key.char == up or key.char == down:
            movement_keys[0] = ''
        elif key.char == left or key.char == right:
            movement_keys[1] = ''
        else:
            print('Invalid character when removing from movement_keys')
            exit()

    else:
        print('Please select either \'set\' or \'remove\' as the first arg when calling manage_movement_keys')
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
    
    elif key.char == stop_key:
        exit()

def set_active_key(key):
    try:
        active_key = key.char
    except Exception as e:
        print(e)

def remove_active_key():
    try:
        active_key = ''
    except Exception as e: 
        print(e)

def manage_click(called_from, key):
    try:
        if called_from == 'set':
            active_key = key.char

        elif called_from == 'remove':
            active_key = ''

        else:
            print('Please select either \'set\' or \'remove\' as the first arg when calling manage_movement_keys')
            exit()

    except Exception as e:
        print(e)

def on_press(key):
    try:
        global no_key_pressed

        # To console
        print('alpha key {0} pressed'.format(key.char))

        # Set movement_keys
        if key.char == up or key.char == down or key.char == left or key.char == right:
            manage_movement_keys('set', key)
            
            # Move the mouse
            if movement_keys != ['', ''] and no_key_pressed == True:
                no_key_pressed = False
                thread = threading.Thread(target=move_mouse)
                thread.start()
  
        else:
            # Handle all clicking / non-moving keys
            manage_click('set', key)
            handle_click(key)
        
        
        
        print("Active keys: " + ' '.join(movement_keys))
    except Exception as e:
        print('special key {0} pressed'.format(key))
        print(e)

def on_release(key):
    print('{0} released'.format(key))
    try:
        # Removes the keys from movement_keys as they are being released
        if key.char == up or key.char == down or key.char == left or key.char == right:
            manage_movement_keys('remove', key)

        else:
            manage_click(key)
        
        print("Active keys: " + ' '.join(movement_keys))
    except Exception as e:
        print(e)



with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True) as listener:
    listener.join()


