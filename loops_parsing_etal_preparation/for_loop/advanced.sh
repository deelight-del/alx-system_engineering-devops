#!/bin/bash

#Passing in arguments into file

for arg; do echo "$arg"; done

#Make backup of all of your txt files.
for file in $(ls *.txt); do cp $file $file'.bak'; done

#Using a py script as command
for i in {1..5}; do ./hello.py ; done
