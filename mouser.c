#include <windows.h>
#include <stdio.h>
#include <conio.h> // for _kbhit() and _getch()

// Function to move the cursor in the specified direction
void moveCursor(char direction, int offset) {
    POINT cursorPos;

    if (!GetCursorPos(&cursorPos)) {
        fprintf(stderr, "Failed to get cursor position. Error: %ld\n", GetLastError());
        return;
    }

    switch (direction) {
        case 'h': // Left
            cursorPos.x -= offset;
            break;
        case 'j': // Down
            cursorPos.y += offset;
            break;
        case 'k': // Up
            cursorPos.y -= offset;
            break;
        case 'l': // Right
            cursorPos.x += offset;
            break;
        default:
            return;
    }

    if (!SetCursorPos(cursorPos.x, cursorPos.y)) {
        fprintf(stderr, "Failed to set cursor position. Error: %ld\n", GetLastError());
    }
}

int main(void) {
    int offset = 50; // Move by 50 pixels
    char key;

    printf("Listening for keys (h/j/k/l). Press 'q' to quit.\n");

    while (1) {
        if (_kbhit()) { // Check if a key has been pressed
            key = _getch(); // Get the pressed key
            if (key == 'q') {
                break; // Exit the loop if 'q' is pressed
            }
            moveCursor(key, offset);
        }
    }

    printf("Exited.\n");
    return 0;
}

