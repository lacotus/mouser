#include <windows.h>
#include <stdio.h>
#include <stdbool.h>

// Global hook handle
HHOOK keyboardHook;

// Track which keys are pressed: index = virtual key code, value = true/false
static bool keysPressed[256] = { false };

// This flag will be used to stop the movement thread
static bool runMovementThread = true;

// Small movement step for smoother motion
static const int STEP_SIZE = 5;

// Delay (in ms) between movement updates - tweak as needed
static const int MOVE_DELAY_MS = 2;

// Forward declarations
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam);
DWORD WINAPI MovementThread(LPVOID lpParam);

// Moves the cursor by (dx, dy)
void moveCursor(int dx, int dy) {
    POINT cursorPos;
    if (!GetCursorPos(&cursorPos)) return;
    cursorPos.x += dx;
    cursorPos.y += dy;
    SetCursorPos(cursorPos.x, cursorPos.y);
}

// Simulate mouse button actions
void simulateClick(DWORD buttonDown, DWORD buttonUp) {
    INPUT input[2] = {0};

    // Button down
    if (buttonDown != 0) {
        input[0].type = INPUT_MOUSE;
        input[0].mi.dwFlags = buttonDown;
    }
    // Button up
    if (buttonUp != 0) {
        input[1].type = INPUT_MOUSE;
        input[1].mi.dwFlags = buttonUp;
    }

    SendInput(2, input, sizeof(INPUT));
}

// Function to block w, a, s, d, j, k, l and q keys
bool ShouldBlockKey(DWORD vkCode)
{
	switch(vkCode) {
		case 'W': case 'A': case 'S': case 'D': 
		case 'J': case 'K': case 'L': case 'Q': 
			return true;
		default:
			return false;
	}
}

// Keyboard hook callback
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT* pKey = (KBDLLHOOKSTRUCT*)lParam;
        DWORD vkCode = pKey->vkCode;

        bool isKeyDown = (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN);
        bool isKeyUp   = (wParam == WM_KEYUP   || wParam == WM_SYSKEYUP);

        // Instead of a lambda, call the function
        if (ShouldBlockKey(vkCode)) {
            if (isKeyDown && !keysPressed[vkCode]) {
                keysPressed[vkCode] = true;
                switch (vkCode) {
                    case 'J':
                        simulateClick(MOUSEEVENTF_LEFTDOWN, 0);
                        break;
                    case 'K':
                        simulateClick(MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP);
                        break;
                    case 'L':
                        simulateClick(MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP);
                        break;
                    case 'Q':
                        runMovementThread = false;
                        PostQuitMessage(0);
                        break;
                }
                return 1; // block the key
            } 
            else if (isKeyUp) {
                keysPressed[vkCode] = false;
                if (vkCode == 'J') {
                    simulateClick(0, MOUSEEVENTF_LEFTUP);
                }
                return 1; // block the key
            }
        }

        // If it's NOT one of our special keys, pass it on
    }
    return CallNextHookEx(keyboardHook, nCode, wParam, lParam);
}

// Thread that handles continuous smooth movement
DWORD WINAPI MovementThread(LPVOID lpParam) {
    while (runMovementThread) {
        // W -> up
        if (keysPressed['W']) {
            moveCursor(0, -STEP_SIZE);
        }
        // A -> left
        if (keysPressed['A']) {
            moveCursor(-STEP_SIZE, 0);
        }
        // S -> down
        if (keysPressed['S']) {
            moveCursor(0, STEP_SIZE);
        }
        // D -> right
        if (keysPressed['D']) {
            moveCursor(STEP_SIZE, 0);
        }

        // Sleep a bit to control speed and CPU usage
        Sleep(MOVE_DELAY_MS);
    }
    return 0;
}

int main() {
    printf("Program started.\n");
    printf("Use W/A/S/D to move, J (hold) for left click, K for middle click, L for right click, Q to quit.\n");

    // Start the thread that will move the cursor
    HANDLE hThread = CreateThread(NULL, 0, MovementThread, NULL, 0, NULL);
    if (!hThread) {
        fprintf(stderr, "Failed to create movement thread!\n");
        return 1;
    }

    // Install keyboard hook
    HINSTANCE hInstance = GetModuleHandle(NULL);
    keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, hInstance, 0);
    if (!keyboardHook) {
        fprintf(stderr, "Failed to install hook! Error: %ld\n", GetLastError());
        runMovementThread = false;
        WaitForSingleObject(hThread, INFINITE);
        CloseHandle(hThread);
        return 1;
    }

    // Main message loop
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Unhook and clean up
    UnhookWindowsHookEx(keyboardHook);

    // Signal thread to stop
    runMovementThread = false;
    WaitForSingleObject(hThread, INFINITE);
    CloseHandle(hThread);

    printf("Program exited.\n");
    return 0;
}

