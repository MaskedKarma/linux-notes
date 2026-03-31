## Loops
A loop is a way to repeat a block of code multiple times without writing it out over and over. They exist because real world tasks are repetitive, checking every server in a list, retrying a connection, processing every line in a log file.

## For Loop
A for loop runs a block of code once for each item in a sequence. Use it when you know what you're iterating over, a list, a string, a range of numbers.

In DevOps you'd use this to loop over a list of servers, config files, or usernames and do something to each one.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
## Range()
Range() generates a sequence of numbers for a for loop to iterate over. It produces numbers one at a time rather than creating a full list in memory.

```python 
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)
```
The three-argument version is range(start, stop, step). Step can be negative for a countdown. Note: stop is always excluded, so range(10, 0, -1) goes down to 1, not 0.

```python
for i in range(10, 0, -1):     # 10, 9, 8 ... 1
    print(i)
```
## While Loop
A while loop keeps running as long as a condition is True. Use it when you don't know in advance how many times you'll need to repeat, waiting for user input, retrying a failed connection, polling until a service is ready.

```python
attempts = 0
while attempts < 3:
    print("Trying to connect...")
    attempts += 1
```
If the condition never becomes False, the loop runs forever, that's called an infinite loop and will hang your program.

## Break
Break immediately exits the loop. Use it when a condition is met and there's no point continuing, you found what you were looking for, or something went wrong.

```python
for number in range(10):
    if number == 5:
        break           # stops the loop entirely at 5
    print(number)       # prints 0, 1, 2, 3, 4
```
## Continue
Continue skips the rest of the current iteration and jumps to the next one. The loop doesn't stop, it just skips that pass. Use it to filter out things you don't want to process.

```python
for number in range(5):
    if number == 2:
        continue        # skips 2, keeps going
    print(number)       # prints 0, 1, 3, 4
```
## += Shorthand
+= adds a value to an existing variable and saves the result back into it. Shorthand to avoid writing the variable name twice.

```python
score = 10
score += 5      # same as score = score + 5
                # score is now 15
```
Works with other operators too: -=, *=, /=. You'll see += 1 constantly in loops as a counter.