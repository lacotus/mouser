import keyboard
import subprocess

def run_program():
    # Replace 'path/to/your/program.exe' with the path to your compiled C program
    program_path = r".\mouser.exe"
    try:
        subprocess.Popen(program_path, shell=True)
    except Exception as e:
        print(f"Failed to run the program: {e}")

# Register the hotkey: Alt+Shift+J
keyboard.add_hotkey('alt+shift+j', run_program)

print("Listening for Alt+Shift+J... Press Ctrl+C to exit.")
try:
    keyboard.wait('esc')  # Wait indefinitely, or replace 'esc' with another exit condition
except KeyboardInterrupt:
    print("Exiting.")

