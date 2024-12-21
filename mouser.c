#include <windows.h>
#include <stdio.h>

int main(void) {
    POINT cursorPos;

    // Step 1: Get the current cursor position
    if (!GetCursorPos(&cursorPos)) {
        fprintf(stderr, "Failed to get cursor position. Error: %ld\n", GetLastError());
        return 1;
    }
    printf("Current Position: (%ld, %ld)\n", cursorPos.x, cursorPos.y);

    // Step 2: Calculate new position (move up by 50 pixels)
    int offset = 50; // how far to move up
    int newX = cursorPos.x;
    int newY = cursorPos.y - offset; // subtract 50 from the Y coordinate

    // Step 3: Move the cursor to the new position
    if (!SetCursorPos(newX, newY)) {
        fprintf(stderr, "Failed to set cursor position. Error: %ld\n", GetLastError());
        return 1;
    }

    printf("Cursor moved to: (%d, %d)\n", newX, newY);
    return 0;
}

