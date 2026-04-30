#!/bin/bash

projectname=$1

setup() {
	mkdir -p "$projectname"/{src,docs,tests} 
	touch "$projectname/README.md" "$projectname/.gitignore"
}

info() {
	echo ""
	echo "User: $USER | Host: $(hostname) | Time: $(date)"
}

summary() {
	echo ""
	echo "Created project '$projectname' with the following structure:"
	ls "$projectname"/
	echo ""
	echo "README.md and .gitignore included. Anything else?"
}

if [ -z "$1" ]; then
	echo "Usage: ./setup-dev-folder.sh <project-name>"
	exit 1
fi

if [ -d "$projectname" ]; then
        echo "Error: '$projectname' already exists."
        exit 1
fi

setup
info
summary
