#!/bin/bash
for i in $(ls *.html); do
	echo "$i"
	NAME=$(ls "$i" | sed -e 's/html/php/') #create a new name for each file that ends with php extension.
	cat beginfile > "$NAME"  #Add first set of lines to new file with new name created above.
	cat "$i" | sed -e '1,25d' | tac | sed -e '1,21d' | tac >> "$NAME"  #Append the middle of the file, after removing some part to the new file.
	cat endfile >> "$NAME";
done
