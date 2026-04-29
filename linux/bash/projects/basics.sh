#!/bin/bash

echo "Hi, $USER, you are currently in '$PWD'"

name=$USER

echo "hi $name"

for i in $(seq 1 5); do
	echo "$i"
done



check_os() {
	cat /etc/os-release
}

check_os
