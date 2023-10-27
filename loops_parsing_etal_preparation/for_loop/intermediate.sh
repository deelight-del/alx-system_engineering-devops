#!/bin/bash

#Using command substitution in place of list.

for file in $(ls); do 
	echo "$file: "
	stat "$file" | head -2;
done

echo "..............................................................................."

# Loop over files and print their names and sizes
for f in *.txt; do
	  echo -n "$f: "
	    du -sh "$f" | awk '{print $1}'
    done
