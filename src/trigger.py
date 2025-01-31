import keyboard
import subprocess

def run_program():
    # Replace 'path/to/your/program.exe' with the path to your compiled C program
    program_path = r"C:\Users\lspie\Software\C\mouser\src\mouser.exe"
    try:
        subprocess.Popen(program_path, shell=True)
    except Exception as e:
        print(f"Failed to run the program: {e}")

try:
    # Register hotkey
    keyboard.add_hotkey('alt+shift+f', run_program)
    print("Listening for Alt+Shift+F... Press Ctrl+C to exit.")
    keyboard.wait('esc')  # Wait until 'esc' is pressed
except KeyboardInterrupt:
    print("Exiting via KeyboardInterrupt")
except Exception:
    # If *anything* else goes wrong, print the full traceback:
    print("An unexpected exception occurred!")
    traceback.print_exc()



# Register the hotkey: Alt+Ctrl+J
#keyboard.add_hotkey('alt+shift+f', run_program)
#
#print("Listening for Alt+Shift+F... Press Ctrl+C to exit.")
#try:
#    keyboard.wait('esc')  # Wait indefinitely, or replace 'esc' with another exit condition
#except KeyboardInterrupt:
#    print("Exiting.")

