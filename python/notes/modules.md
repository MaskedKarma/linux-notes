# Modules

## import
`import` loads a module and makes its functions available in your script. Modules are pre-written Python files that ship with the standard library or are installed via pip — you import them instead of writing the logic yourself.

```python
import random
import time
```
When Python sees `import random` it finds the module, loads it once, and binds it to the name `random`. Every call to `random.something` reaches into that loaded module.

## random
The `random` module generates random values. Useful for testing, simulating unpredictable events, and load balancing.

```python
import random

servers = ["web-01", "web-02", "web-03", "web-04"]

print(random.choice(servers))       # picks one item at random from any sequence
print(random.randint(1, 100))       # returns a random integer — both ends inclusive
random.shuffle(servers)             # randomises the list order in-place, returns None
print(servers)
```

## time
The `time` module lets you pause execution and measure how long things take.

```python
import time

servers = ["web-01", "web-02", "web-03"]

for server in servers:
    print(f"Pinging {server}...")
    time.sleep(1)                   # pauses for 1 second — accepts floats e.g. 0.5
    print(f"{server} OK")

start = time.time()                 # current time as a float — seconds since Jan 1 1970
time.sleep(2)
end = time.time()
print(f"Took {end - start:.2f} seconds")    # subtract to get elapsed time
```
`time.sleep()` is used in scripts that poll an API or ping a server — you don't want to hit something thousands of times a second. `time.time()` is used to benchmark how long a script takes to run.