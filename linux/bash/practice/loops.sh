#!/bin/bash

for i in 1 2 3 4 5; do
	echo "number $i"
done



for i in $(seq 1 5); do
	echo "number $i"
done



count=0
while [ $count -lt 6 ]; do
	echo "Count is $count"
	count=$((count +1))
done
