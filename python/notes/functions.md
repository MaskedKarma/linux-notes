## Functions
A function is a reusable block of code that runs when you call it. They exist to avoid repeating yourself, if you're writing the same logic more than once, it belongs in a function.

## Basic Structure
`def` defines the function, followed by a name, parentheses for parameters, and a colon. The indented block beneath it is the body, the code that runs when called.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Adam")       # calling it, this is what actually runs it
```
Parameters are the placeholders defined in the function. Arguments are the real values you pass in when calling it.

## Return vs Print
`return` sends a value back to whoever called the function so it can be used, `print` just displays it and the value is gone.

```python
def add(a, b):
    return a + b        # value comes back, can be stored or used

result = add(3, 4)
print(result)           # 7
```
## Default Parameters
Default parameters give a value a fallback if nothing is passed in. Useful when an argument is optional.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Adam")               # Hello, Adam
greet("Adam", "Welcome")    # Welcome, Adam
```
Never use a mutable value like a list or dictionary as a default, Python creates it once at definition time, not each call, which causes bugs that are hard to track down.

## Scope
A variable created inside a function only exists inside that function.

```python
def greet():
    message = "Hello"   # only exists inside greet

print(message)          # NameError, message doesn't exist out here
```

## The Pattern
A well-written function does one job and does it cleanly, it doesn't reach out for input or print its own results. The caller handles what goes in and what happens with what comes back. This makes functions reusable anywhere without them caring where the data came from.

```python
def add(a, b):          # function does the work
    return a + b

x = int(input("First number: "))    # caller handles input
y = int(input("Second number: "))
print(add(x, y))                    # caller handles output
```


