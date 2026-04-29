#!/bin/bash

projectname=$1

setup() {
	        mkdir -p $projectname/{src,docs,tests} 
		touch $projectname/README.md $projectname/.gitignore
}

date=$(date)
info() {
		echo "Hi, current user is $USER with the host being $(hostname), it's currently $date."
}

summary() {
	echo "I have created a directory for '$projectname', a README, .gitignore, and sub-folders for src, docs and tests. Anything else?"
}


if [ -z "$1" ]; then
	echo "Usage: ./setup-dev-folder.sh <project-name>"
	exit 1
else
	setup
	info
	summary
fi
