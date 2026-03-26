# Linux Commands

Commands I'm learning, with explanations and real-world use cases.

## Navigation
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `pwd` | Print current directory path | `pwd` | First thing to run when you SSH into a server to confirm where you are |
| `ls` | List files in current folder | `ls` | Checking what's in a directory before doing anything to it |
| `ls -la` | List all files including hidden, with details | `ls -la` | Checking permissions, finding hidden config files like `.env` |
| `cd` | Change directory | `cd ~/dev` | Navigating to your project folder |
| `cd ~` | Go to home directory | `cd ~` | Instantly return home from anywhere |
| `cd ..` | Go up one folder | `cd ..` | Moving up one level in a project structure |
| `cd -` | Go to previous directory | `cd -` | You ran a command somewhere else and want to go back instantly |

## Files and Folders
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `mkdir` | Create a folder | `mkdir projects` | Setting up a new project directory structure |
| `touch` | Create an empty file | `touch notes.txt` | Creating a placeholder file or a new script before editing it |
| `cp` | Copy a file | `cp file1.txt backup.txt` | Backing up a config file before editing it |
| `mv` | Move or rename a file | `mv old.txt new.txt` | Renaming a file or moving it to a different folder |
| `rm` | Delete a file | `rm notes.txt` | Cleaning up temporary files |
| `rm -r` | Delete a folder and contents | `rm -r oldfolder` | Removing an old project or build folder entirely |

## Reading Files
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `cat` | Print file contents to terminal | `cat README.md` | Quickly checking a config file or log without opening an editor |
| `nano` | Open file in terminal text editor | `nano config.txt` | Editing a config file directly on a server with no GUI available |

## Finding Things
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `find . -name "file.txt"` | Find a file by name from current folder | `find . -name "README.md"` | You know a file exists but can't remember where you put it |
| `find . -type f` | Find only files | `find . -type f` | Listing every file in a project recursively |
| `find . -type d` | Find only directories | `find . -type d` | Checking the folder structure of a project |
| `grep "text" file` | Search for text inside a file | `grep "error" log.txt` | Finding a specific error message in a log file |
| `grep -i "text" file` | Case-insensitive search | `grep -i "linux" README.md` | Searching when you're not sure of the capitalisation |
| `grep -r "text" .` | Search recursively through all files | `grep -r "mkdir" .` | Finding which file contains a specific config value or function |
| `grep -n "text" file` | Show line numbers with matches | `grep -n "cd" commands.md` | Finding the exact line to jump to in an editor |
| `grep -c "text" file` | Count matching lines | `grep -c "ERROR" app.log` | Quickly seeing how many errors occurred in a log file |

## Permissions
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `ls -la` | Show permissions for all files | `ls -la` | Diagnosing permission errors — checking who can read/write/execute |
| `chmod 600 file` | Owner read/write only | `chmod 600 .env` | Locking down secrets — SSH keys, .env files, API tokens |
| `chmod 644 file` | Owner read/write, everyone read | `chmod 644 index.html` | Web files that a server process needs to read but not modify |
| `chmod 755 file` | Owner full, everyone read/execute | `chmod 755 deploy.sh` | Scripts your whole team needs to run but only you should edit |
| `chmod +x file` | Add execute permission | `chmod +x script.sh` | Making a new bash script runnable after writing it |

## Permissions reference
- `r` = read = 4
- `w` = write = 2
- `x` = execute = 1
- `7` = rwx (full), `6` = rw-, `5` = r-x, `4` = r--
- First character of `ls -la`: `-` = file, `d` = directory
- Three groups: owner / group / everyone else
- Common combinations: 600 = secrets, 644 = regular files, 755 = scripts, 700 = private folders

## Processes
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `ps` | Show processes in current terminal session | `ps` | Quick check of what's running in your current shell |
| `ps aux` | Show all running processes on the system | `ps aux` | Getting a full picture of everything running on a server |
| `ps aux \| grep name` | Find a specific running process | `ps aux \| grep nginx` | Checking if a specific service is actually running |
| `top` | Live view of system resources and processes | `top` | Diagnosing high CPU or memory usage on a slow server |
| `id` | Show your user ID and group | `id` | Confirming which user and groups you're running as |

## Processes reference
- PID = unique process ID — used to kill or manage a specific process
- %CPU = percentage of CPU being used
- %MEM = percentage of RAM being used
- TTY = which terminal the process is attached to (? = background process)
- STAT: S = sleeping, R = running, I = idle, < = high priority
- The pipe `|` sends output of one command as input to another

## Package Management
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `sudo pacman -Syu` | Update package database and upgrade all packages | `sudo pacman -Syu` | Weekly maintenance — keeping system secure and up to date |
| `sudo pacman -S package` | Install a package | `sudo pacman -S git` | Installing a new tool you need |
| `sudo pacman -R package` | Remove a package | `sudo pacman -R git` | Cleaning up software you no longer need |
| `sudo pacman -Rs package` | Remove package and unused dependencies | `sudo pacman -Rs htop` | Cleaner removal that doesn't leave orphaned packages behind |
| `pacman -Ss term` | Search online repositories for a package | `pacman -Ss python` | Finding the correct package name before installing |
| `pacman -Qs term` | Search locally installed packages | `pacman -Qs python` | Checking if something is already installed without hitting the internet |
| `pacman -Qi package` | Show detailed info about installed package | `pacman -Qi python` | Checking exact version, install date, and dependencies |
| `pacman -Qe` | List all explicitly installed packages | `pacman -Qe` | Auditing what you've installed on a machine |
| `paru -S package` | Install from AUR or official repos | `paru -S visual-studio-code-bin` | Installing software not in the official repos |
| `paru -Syu` | Update everything including AUR packages | `paru -Syu` | Full system update including community packages |

## Users and Groups
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `whoami` | Print current username | `whoami` | Confirming which user you're running as on a server |
| `id` | Show UID, GID and all groups | `id` | Diagnosing permission issues — checking if you're in the right group |
| `groups` | Show groups current user belongs to | `groups` | Checking if your user has docker or wheel group access |
| `cat /etc/passwd` | View all system users | `cat /etc/passwd` | Auditing users on a server, finding service account names |
| `cat /etc/group` | View all groups and members | `cat /etc/group` | Checking which users belong to which groups |
| `sudo cat /etc/shadow` | View encrypted passwords (root only) | `sudo cat /etc/shadow` | Security auditing — verifying password policies |

## Users reference
- UID = user ID number, every user has a unique one
- GID = group ID number
- wheel group = sudo access on Arch-based systems
- www-data = typical user web servers run as
- Principle of least privilege: services run as limited users with only the permissions they need

## Disk Usage
| Command | What it does | Example | When you'd use it |
|---------|-------------|---------|-------------------|
| `df -h` | Show how full each filesystem/drive is | `df -h` | Server alerts on disk space — first command to run to see which drive is full |
| `du -sh folder` | Show total size of a specific folder | `du -sh ~` | Finding out how much space your home folder is using |
| `du -sh folder/*` | Show size of each item inside a folder | `du -sh ~/dev/*` | Identifying which project is taking up the most space |
| `du -sh ~/* \| sort -h` | Show home folder contents sorted by size | `du -sh ~/* \| sort -h` | Finding the biggest space consumers when a server is running low |

## SSH reference (conceptual)
- SSH = Secure Shell — lets you control remote servers from your terminal
- Uses public/private key pairs — private key stays on your machine, public key goes on server
- Key-based auth is more secure than passwords — keys are not brute-forceable
- `ssh-keygen -t ed25519` — generate a key pair (covered properly in AWS section)
- `ssh username@ip` — connect to a remote server
- `chmod 600 ~/.ssh/id_rsa` — private key must be owner read/write only, SSH refuses to work otherwise
- Real use: every cloud server you manage will be accessed via SSH