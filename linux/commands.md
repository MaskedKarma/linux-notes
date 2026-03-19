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

## Permissions
| Command | What it does | Example |
|---------|-------------|---------|
| `ls -la` | Show permissions for all files | `ls -la` |
| `chmod 755 file` | Set rwx for owner, rx for others | `chmod 755 script.sh` |
| `chmod 644 file` | Set rw for owner, r for others | `chmod 644 config.txt` |
| `chmod 600 file` | Set rw for owner only | `chmod 600 secret.txt` |

## Permissions reference
- r = read = 4
- w = write = 2  
- x = execute = 1
- 7 = rwx, 6 = rw-, 5 = r-x, 4 = r--

## Processes
| Command | What it does | Example |
|---------|-------------|---------|
| `ps` | Show processes in current session | `ps` |
| `ps aux` | Show all running processes | `ps aux` |
| `ps aux | grep name` | Find a specific process | `ps aux | grep firefox` |
| `top` | Live view of system processes and resources | `top` |