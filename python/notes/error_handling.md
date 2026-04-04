# Error Handling

## try/except
`try/except` lets you handle errors without crashing the program. Python tries the code in the `try` block — if something goes wrong, it jumps to the matching `except` block instead of stopping.

```python
servers = ["web-01", "web-02", "web-03"]

try:
    index = int(input("Pick a server by number: "))
    print(f"You picked: {servers[index]}")
except ValueError:                          # raised when int() gets something non-numeric like "abc"
    print("That's not a valid number.")
except IndexError:                          # raised when the number is valid but outside the list range
    print("No server at that index.")
```
In real DevOps scripts you can't control what users type or whether a network call succeeds. Without `try/except`, any unexpected input crashes the whole script.

## not in
`not in` checks whether a value is absent from a sequence. It's the readable alternative to `if x in list == False`.

```python
allowed = ["web-01", "web-02", "web-03"]

server = input("Enter server name: ")
if server not in allowed:
    print(f"{server} is not a recognised server.")
```
Use it to validate input against a whitelist before taking action.

## continue inside except
`continue` skips the rest of the current loop iteration and moves to the next one. Inside an `except` block it lets you log a failure and carry on rather than stopping everything.

```python
servers = ["web-01", "web-02", "OFFLINE", "web-04"]

for server in servers:
    try:
        if server == "OFFLINE":
            raise ConnectionError("Server is offline")  # 'raise' manually triggers an exception
        print(f"Connected to {server}")
    except ConnectionError as e:                        # 'as e' captures the exception so you can read its message
        print(f"Skipping {server}: {e}")
        continue                                        # move to the next server, don't stop the loop
```
In real infrastructure work one unreachable server shouldn't halt checks on the other 49. `continue` keeps the loop resilient.
