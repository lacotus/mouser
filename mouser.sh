#! /bin/sh

# Get x and y cords of mouse location for the start
eval $(xdotool getmouselocation --shell)
echo "Mouse starting position: " $X $Y
notify-send "Mouser was ran"

xinput get-feedbacks 5 | grep -A2 --line-buffered RawKeyRelease | while read -n 1 $input; 
do
	# Get x and y cords again
	eval $(xdotool getmouselocation --shell)
	echo "input: " $input
	# xinput test 5 | read -t 0.1 -n 1 input

	# Check input
	
	# Single direction
	if [ "$input" == "s" ] || [ "$input" == "S" ]; then
	       	# a. Displays X location before change
		echo $X

		# b. Does change, assigns cursor to new location
		((X = $X - 10))
		xdotool mousemove $X $Y
       		
		continue
 	
	elif [ "$input" == "f" ] || [ "$input" == "F" ]; then
		# a. - see first if block
		echo $X

		# b. - see first if block
		((X = $X + 10))
		xdotool mousemove $X $Y

		continue

	elif [ "$input" == "e" ] || [ "$input" == "E" ]; then
		if [ "$input" == "s" ] || [ "$input" == "S" ]; then
			echo "e and s are being pressed"
		fi
		# a. - see first if block
		echo $Y

		# b. - see first if block
		((Y = $Y - 10))
		xdotool mousemove $X $Y
		
		continue
	elif [ "$input" == "d" ] || [ "$input" == "D" ]; then
		# a. - see first if block
		echo $Y

		# b. - see first if block
		((Y = $Y + 10))
		xdotool mousemove $X $Y

		continue

	elif [ "$input" == ";" ] || [ "$input" == ":" ]; then
		echo $X $Y
		break			
	# Up and left + up and right
	elif [ "$input" == "e" ] && [ "$input" == "s" ]; then
		echo $X $Y
		echo "e and s are pressed"
		continue
	fi
done

