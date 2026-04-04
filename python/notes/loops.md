## Loops
A loop repeats a block of code without writing it out over and over. Real world tasks are repetitive — checking every server in a list, retrying a connection, processing every line in a log file.

## for Loop
A `for` loop runs once for each item in a sequence. Use it when you know what you're iterating over — a list, a string, or a range of numbers.
```python
servers = ["web01", "web02", "db01"]
for server in servers:
    print(server)
```
In DevOps you'd use this to loop over servers, config files, or usernames and do something to each one.

## range()
`range()` generates a sequence of numbers for a `for` loop to iterate over. Produces numbers one at a time rather than building a full list in memory.
```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)
```
The three-argument version is `range(start, stop, step)`. Step can be negative for a countdown. Stop is always excluded — `range(10, 0, -1)` goes down to 1, not 0.
```python
for i in range(10, 0, -1):  # 10, 9, 8 ... 1
    print(i)
```

## while Loop
A `while` loop keeps running as long as a condition is True. Use it when you don't know in advance how many times you'll need to repeat — waiting for user input, retrying a failed connection, polling until a service is ready.
```python
attempts = 0
while attempts < 3:
    print("Trying to connect...")
    attempts += 1
```
If the condition never becomes False the loop runs forever — that's an infinite loop and it will hang your program.

## break
`break` exits the loop immediately. Use it when a condition is met and there's no point continuing.
```python
for number in range(10):
    if number == 5:
        break
    print(number)       # prints 0, 1, 2, 3, 4
```

## continue
`continue` skips the rest of the current iteration and jumps to the next one. The loop doesn't stop — it just skips that pass.
```python
for number in range(5):
    if number == 2:
        continue
    print(number)       # prints 0, 1, 3, 4
```

## += shorthand
`+=` adds a value to an existing variable and stores the result back into it. Shorthand to avoid writing the variable name twice.
```python
score = 10
score += 5      # same as score = score + 5
                # score is now 15
```
Works with other operators too: `-=`, `*=`, `/=`. You'll see `+= 1` constantly in loops as a counter.