#include <iostream>

int main()
{
	std::cout << "Hello, world!";
	int result = system("systemsettings");
	
	// Get cursor position:
	
	typedef struct Point {
		int x, y;
	} POINT, *PPOINT, *NPOINT, *LPOINT;

	Point p;
	int pos_x, pos_y;
	if (GetCursorPos(&p)) {
		//  Cursor position in p.x and p.y
		pos_x = p.x;
		pos_y = p.y;
	} else {
		std::cout << "GetCursorPosition() failed";
	}
}
