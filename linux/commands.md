# Linux Commands

Commands I'm learning, with explanations.

## Navigation
| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Print current directory path | `pwd` |
| `ls` | List files in current folder | `ls` |
| `ls -la` | List all files including hidden, with details | `ls -la` |
| `cd` | Change directory | `cd ~/dev` |
| `cd ~` | Go to home directory | `cd ~` |
| `cd ..` | Go up one folder | `cd ..` |
| `cd -` | Go to previous directory | `cd -` |

## Files and Folders
| Command | What it does | Example |
|---------|-------------|---------|
| `mkdir` | Create a folder | `mkdir projects` |
| `touch` | Create an empty file | `touch notes.txt` |
| `cp` | Copy a file | `cp file1.txt backup.txt` |
| `mv` | Move or rename a file | `mv old.txt new.txt` |
| `rm` | Delete a file | `rm notes.txt` |
| `rm -r` | Delete a folder and contents | `rm -r oldfolder` |

## Reading Files
| Command | What it does | Example |
|---------|-------------|---------|
| `cat` | Print file contents to terminal | `cat README.md` |
| `nano` | Open file in terminal text editor | `nano config.txt` |

## Finding Things
| Command | What it does | Example |
|---------|-------------|---------|
| `find . -name "file.txt"` | Find a file by name from current folder | `find . -name "README.md"` |
| `find . -type f` | Find only files | `find . -type f` |
| `find . -type d` | Find only directories | `find . -type d` |
| `grep "text" file` | Search for text inside a file | `grep "error" log.txt` |
| `grep -i "text" file` | Case-insensitive search | `grep -i "linux" README.md` |
| `grep -r "text" .` | Search recursively through all files | `grep -r "mkdir" .` |
| `grep -n "text" file` | Show line numbers with matches | `grep -n "cd" commands.md` |
| `grep -c "text" file` | Count matching lines | `grep -c "Command" commands.md` |

## Permissions
| Command | What it does | Example |
|---------|-------------|---------|
| `ls -la` | Show permissions for all files | `ls -la` |
| `chmod 600 file` | Owner read/write only — for secrets | `chmod 600 .env` |
| `chmod 644 file` | Owner read/write, everyone read | `chmod 644 index.html` |
| `chmod 755 file` | Owner full, everyone read/execute | `chmod 755 deploy.sh` |
| `chmod +x file` | Add execute permission | `chmod +x script.sh` |

## Permissions reference
- `r` = read = 4
- `w` = write = 2
- `x` = execute = 1
- `7` = rwx (full), `6` = rw-, `5` = r-x, `4` = r--
- First character of ls -la: `-` = file, `d` = directory
- Three groups: owner / group / everyone else

## Processes
| Command | What it does | Example |
|---------|-------------|---------|
| `ps` | Show processes in current terminal session | `ps` |
| `ps aux` | Show all running processes on the system | `ps aux` |
| `ps aux \| grep name` | Find a specific running process | `ps aux \| grep firefox` |
| `top` | Live view of system resources and processes | `top` |
| `id` | Show your user ID and group | `id` |

## Processes reference
- PID = unique process ID number
- %CPU = percentage of CPU being used
- %MEM = percentage of RAM being used
- TTY = which terminal the process is attached to (? = background)
- STAT: S = sleeping, R = running, I = idle, < = high priority
- The pipe `|` sends output of one command as input to another

## Package Management
| Command | What it does | Example |
|---------|-------------|---------|
| `sudo pacman -Syu` | Update package database and upgrade all packages | `sudo pacman -Syu` |
| `sudo pacman -S package` | Install a package | `sudo pacman -S git` |
| `sudo pacman -R package` | Remove a package | `sudo pacman -R git` |
| `pacman -Ss term` | Search repositories for a package | `pacman -Ss python` |
| `pacman -Qs term` | Search locally installed packages | `pacman -Qs python` |
| `pacman -Qi package` | Show detailed info about installed package | `pacman -Qi python` |
| `pacman -Qe` | List all explicitly installed packages | `pacman -Qe` |
| `paru -S package` | Install from AUR or official repos | `paru -S visual-studio-code-bin` |
| `paru -Syu` | Update everything including AUR packages | `paru -Syu` |

## Users and Groups
| Command | What it does | Example |
|---------|-------------|---------|
| `whoami` | Print current username | `whoami` |
| `id` | Show UID, GID and all groups | `id` |
| `groups` | Show groups current user belongs to | `groups` |
| `cat /etc/passwd` | View all system users | `cat /etc/passwd` |
| `cat /etc/group` | View all groups and members | `cat /etc/group` |
| `sudo cat /etc/shadow` | View encrypted passwords (root only) | `sudo cat /etc/shadow` |

## Users reference
- UID = user ID number, every user has a unique one
- GID = group ID number
- wheel group = sudo access on Arch-based systems
- Principle of least privilege: services run as limited users with only permissions they need

## Disk Usage
| Command | What it does | Example |
|---------|-------------|---------|
| `df -h` | Show disk space on all filesystems | `df -h` |
| `du -sh folder` | Show total size of a folder | `du -sh ~` |
| `du -sh folder/*` | Show size of each item in a folder | `du -sh ~/dev/*` |
| `du -sh ~/* \| sort -h` | Show home folder sizes sorted by size | `du -sh ~/* \| sort -h` |

## SSH reference (conceptual)
- SSH = Secure Shell, lets you control remote computers from terminal
- Uses public/private key pairs — private key stays on your machine, public key goes on server
- Key-based auth is more secure than passwords — keys are not brute-forceable
- `ssh-keygen -t ed25519` — generate a key pair (covered properly in AWS section)
- `ssh username@ip` — connect to a remote server
- Private key files must be chmod 600 — SSH refuses to work if permissions are too open 