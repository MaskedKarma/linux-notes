Bash Scripting

Bash is the native language of the Linux shell. In DevOps it's everywhere — CI/CD pipelines, Docker entrypoint scripts, startup scripts, cron jobs. Every server you'll work with runs Linux, and when you SSH in to deploy, run backups, or restart services, you're writing Bash.

The Shebang
Every Bash script starts with this on the very first line. It tells the system which interpreter to use when the file is executed.
bash#!/bin/bash
Always include it — scripts get run by other people, CI/CD pipelines, and cron jobs where you can't guarantee how they'll be invoked.

Creating and Running a Script
bashtouch hello.sh
chmod +x hello.sh       # makes it executable
./hello.sh              # runs it
./ means "run this file from the current directory." Linux doesn't look in the current directory for executables by default — only in directories listed in $PATH.

Variables
No spaces around the = — Bash will interpret it as a command and throw an error.
bashname="Justin"
echo "Hello, $name"
To capture command output into a variable, use $() — this runs the command inside and returns the output as a string.
bashcurrent_date=$(date)
echo "Today is $current_date"

User Input
read captures input from the user and stores it in a variable.
bashecho "What's your name?"
read name
echo "Hello, $name!"

Conditionals
bashif [ "$name" == "Justin" ]; then
    echo "Hey Justin!"
elif [ "$name" == "Adam" ]; then
    echo "Hey Adam!"
else
    echo "Hey stranger!"
fi
Key differences from Python — conditions go inside [ ] with spaces on both sides. The block ends with fi. Always quote variables inside conditions — "$name" not $name — to avoid errors if the variable is empty.
'-z' checks if a string is empty — used to validate that an argument was actually passed.

Loops
For loop with a range, using seq to generate numbers.
bashfor i in $(seq 1 5); do
    echo "Number $i"
done
While loop. Bash uses -lt, -gt, -eq, -ne for comparisons inside [ ] instead of <, >, ==. $((count + 1)) is arithmetic expansion — how you do maths in Bash.
bashcount=0
while [ $count -lt 5 ]; do
    echo "Count is $count"
    count=$((count + 1))
done

Functions
Arguments are positional — $1 is the first argument passed, $2 the second. There are no named parameters like Python.
bashgreet() {
    echo "Hello, $1!"
}

greet "Justin"

$USER vs $(date)
The difference is what they're referencing.
$USER is an environment variable — a value that already exists in your shell's environment, set by the system at login. You just reference it with $.
$(date) is command substitution — you're running the date command and capturing its output. You need the parentheses because date isn't a variable, it's a program you need to execute.
bashecho $USER              # reads a variable that already exists
echo $(date)            # runs a command and uses its output

exit 0 and exit 1
When a script finishes normally it exits with code 0 automatically — success. exit 1 explicitly signals failure. This matters when something else is running your script — a CI/CD pipeline checks the exit code and stops if it sees a failure.
bashif [ -z "$1" ]; then
    echo "Usage: ./script.sh <name>"
    exit 1              # stops immediately, signals failure
fi
Without exit 1 the script would print the message and keep executing. Use it any time your script hits an error condition and can't continue.

Useful Built-in Variables
bashecho $HOME      # your home directory
echo $USER      # current username
echo $PWD       # current directory
echo $0         # name of the script itself
echo $#         # number of arguments passed to the script