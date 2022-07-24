#!/user/bin/env python3

from pynput import keyboard
import mouse
import subprocess
import threading

# Comments with letters are based on 'Program map' in Notes.txt of the src directory

# -=- A -=-
no_key_pressed = True

movement_keys = ['', ''] # spot 0 represents up/down while spot 1 represents left / right. captures movement.
active_key = '' # for reading which control is active (probably used mostly for click_left and dragging)
speed_key = '' # for reading if speed is set to slow or turbo
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

# -=- B -=-
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

# -=- C -=-
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

# -=- D -=-
def manage_press(key):
    try:

        # Sort input into Movement, Click, Scroll/Stop, Speed
        
        # Movement
        if key.char == up or key.char == down or key.char == left or key.char == right:
            
            # Movement keys, sets value based on what is read
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

        # Click 
        elif key.char == click_left or key.char == click_middle or key.char == click_right:
            
            # Sets active key
            global active_key
            active_key = key.char

            # Calls click
            handle_click(key)

        # Scroll/Stop
        elif key.char == scroll_up or key.char == scroll_down or key.char == stop_key:
            
            # Call click, no need to record if these keys are being held yet
            handle_click(key)

        elif key == speed_turbo or key == speed_slow:
            # TODO - handle speed keys
            global speed_key
            speed_key = speed_turbo
            

    except Exception as e:
        print(e)    

# -=- E -=-
def manage_release(key):
    try:
        
        # Sort input into Movement, Click, Speed

        # Movement
        if key.char == up or key.char == down or key.char == left or key.char == right:
            
            # Movement keys, sets value based on what is read
            if key.char == up:
                movement_keys[0] = ''
        
            elif key.char == down:
                movement_keys[0] = ''

            elif key.char == left:
                movement_keys[1] = ''

            elif key.char == right:
                movement_keys[1] = ''
            else:
                print('Invalid character when adding to movement_keys')
                exit()

        # Click
        elif key.char == click_left or key.char == click_middle or key.char == click_right:
            
            # Sets active key
            global active_key
            active_key = ''

 

    except Exception as e:
        print(e)

# -=- F -=-
def on_press(key):
    try:
        manage_press(key)
        
        print("Movement keys: " + ' '.join(movement_keys))
        print("Speed key: " + speed_key)
        print("Active key: " + active_key)
    except Exception as e:
        print('special key {0} pressed'.format(key))
        print(e)

# -=- G -=-
def on_release(key):
    print('{0} released'.format(key))
    try:
        manage_release(key)
        
        print("Active keys: " + ' '.join(movement_keys))
    except Exception as e:
        print(e)

# -=- H -=-
# Starts threading move_mouse()
thread = threading.Thread(target=move_mouse)
thread.start()

# -=- I -=-
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True) as listener:
    listener.join()


