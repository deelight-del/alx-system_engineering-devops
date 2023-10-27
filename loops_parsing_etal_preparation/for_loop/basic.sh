#!/bin/bash
for number in 1 2 3 4 5 6 7 8; do echo $number; done

#Using brace expansion...
echo "............................................................................"
for num in {30..50..5}; do 
	echo -n "Square of $num is" 
	echo " $(($num * $num)) "; done

echo "........................................................................."

