#include <windows.h>
#include <stdio.h>

HHOOK keyboardHook; // Global hook handle
int offset = 25;    // Cursor movement offset

// Function to move the cursor in a specific direction
void moveCursor(int dx, int dy) {
    POINT cursorPos;

    if (!GetCursorPos(&cursorPos)) {
        fprintf(stderr, "Failed to get cursor position. Error: %ld\n", GetLastError());
        return;
    }

    cursorPos.x += dx;
    cursorPos.y += dy;

    if (!SetCursorPos(cursorPos.x, cursorPos.y)) {
        fprintf(stderr, "Failed to set cursor position. Error: %ld\n", GetLastError());
    }
}

// Function to simulate a mouse click
void simulateClick(DWORD buttonDown, DWORD buttonUp) {
    INPUT input[2] = {0};

    input[0].type = INPUT_MOUSE;
    input[0].mi.dwFlags = buttonDown;

    input[1].type = INPUT_MOUSE;
    input[1].mi.dwFlags = buttonUp;

    SendInput(2, input, sizeof(INPUT));
}

// Hook procedure to intercept and block keyboard input
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0 && wParam == WM_KEYDOWN) {
        KBDLLHOOKSTRUCT *pKeyBoard = (KBDLLHOOKSTRUCT *)lParam;

        switch (pKeyBoard->vkCode) {
            case 'W':
                moveCursor(0, -offset); // Move up
                return 1; // Block the key
            case 'A':
                moveCursor(-offset, 0); // Move left
                return 1; // Block the key
            case 'S':
                moveCursor(0, offset); // Move down
                return 1; // Block the key
            case 'D':
                moveCursor(offset, 0); // Move right
                return 1; // Block the key
            case 'J':
                simulateClick(MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP); // Left click
                return 1; // Block the key
            case 'K':
                simulateClick(MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP); // Middle click
                return 1; // Block the key
            case 'L':
                simulateClick(MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP); // Right click
                return 1; // Block the key
            case 'Q': // Exit if 'Q' is pressed
                PostQuitMessage(0);
                return 1; // Block the key
        }
    }

    return CallNextHookEx(keyboardHook, nCode, wParam, lParam); // Pass to the next hook
}

int main() {
    printf("Program started. Use w/a/s/d to move, j/k/l for clicks, q to quit.\n");

    HINSTANCE hInstance = GetModuleHandle(NULL);
    MSG msg;

    // Set the keyboard hook
    keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, hInstance, 0);
    if (!keyboardHook) {
        fprintf(stderr, "Failed to install hook! Error: %ld\n", GetLastError());
        return 1;
    }

    // Message loop
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Unhook and clean up
    UnhookWindowsHookEx(keyboardHook);
    printf("Program exited.\n");
    return 0;
}

