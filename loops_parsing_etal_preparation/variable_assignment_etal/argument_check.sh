#!/bin/bash

#Check for the number of arguments passed to a script

N_ARGS=10
E_BADARGS=85

if [ $# -gt $N_ARGS ]
then
	echo "Usage: 'basename $0' accepts less than 10 arguments"
	exit $E_BADARGS
fi

check_int()
{
	value=$1
	if [[ $value =~ ^[0-9]+$ ]]; then
		return 0
	else
		return 1
	fi
}

for arg in $@; do
	if check_int "$arg"; then
		echo "$arg is an integer"
	else
		echo "$arg is not an integer"
		exit "$E_BADARGS"
	fi
done
