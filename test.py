"""
tiny_mouse.py
Ctrl+Shift+M toggles keyboard‑mouse mode.
When active:
    w / a / s / d  → move cursor
    j / k / l      → left‑, middle‑, right‑click
Esc               → exit program
"""
from pynput import keyboard, mouse
import threading
import time

MOVE_STEP   = 25      # pixels per tap
MOVE_DELAY  = 0.02    # hold‑down repeat rate (seconds)

m          = mouse.Controller()
mouse_mode = False    # toggled by Ctrl+Shift+M
pressed    = set()    # keys currently held down
stop_event = threading.Event()

def move_loop():
    """Smooth movement while keys are held."""
    while not stop_event.is_set():
        if mouse_mode:
            dx = (-MOVE_STEP if 'a' in pressed else 
                   MOVE_STEP if 'd' in pressed else 0)
            dy = (-MOVE_STEP if 'w' in pressed else 
                   MOVE_STEP if 's' in pressed else 0)
            if dx or dy:
                x, y = m.position
                m.position = (x + dx, y + dy)
        time.sleep(MOVE_DELAY)

def on_press(key):
    global mouse_mode
    try:
        k = key.char.lower()
    except AttributeError:
        k = None

    # toggle hot‑key: ctrl+shift+m
    if key == keyboard.KeyCode.from_char('m') \
       and keyboard.Key.ctrl in pressed \
       and keyboard.Key.shift in pressed:
        mouse_mode = not mouse_mode
        print(f"[INFO] Mouse mode {'ON' if mouse_mode else 'OFF'}")

    # track held keys
    pressed.add(key)
    if k in 'wasd':
        pressed.add(k)

    # clicks
    if mouse_mode and k in 'jkl':
        button = { 'j': mouse.Button.left,
                   'k': mouse.Button.middle,
                   'l': mouse.Button.right }[k]
        m.click(button)

    # graceful exit
    if key == keyboard.Key.esc:
        stop_event.set()
        return False        # stop listener

def on_release(key):
    pressed.discard(key)
    try:
        pressed.discard(key.char.lower())
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press,
                             on_release=on_release)
listener.start()

threading.Thread(target=move_loop, daemon=True).start()
listener.join()

