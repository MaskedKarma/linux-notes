## Lists
A list is an ordered collection of values stored in a single variable. They exist because most real data isn't a single value, it's a group of things. A list of servers, a list of usernames, a list of IP addresses.

## Creating a List
Lists are defined with square brackets, with each item separated by a comma. They can hold any data type, even mixed.

```python
servers = ["web01", "web02", "db01"]
ages = [25, 31, 47]
mixed = ["admin", 3, True]
empty = []
```

## Accessing Items
Lists are zero-indexed, the first item is at position 0, not 1. This is called indexing.

```python
servers = ["web01", "web02", "db01"]
print(servers[0])       # web01
print(servers[1])       # web02
```
Negative indexing counts from the end. -1 is always the last item.
```python
print(servers[-1])      # db01
print(servers[-2])      # web02
```

## Modifying a List
`append()` adds an item to the end of the list.

```python
servers.append("db02")  # ["web01", "web02", "db01", "db02"]
```
`remove()` removes the first matching value.
```python
servers.remove("web02") # ["web01", "db01", "db02"]
```
You can replace an item directly by assigning to its index.
```python
servers[0] = "web03"    # replaces web01 with web03
```

## Useful Methods
`len()` returns the number of items in a list. Useful when looping or validating.

```python
print(len(servers))     # 3
```
`sort()` sorts the list in place, alphabetically or numerically.
```python
servers.sort()          # ["db01", "web01", "web02"]
```
`reverse()` reverses the current order of the list in place.
```python
servers.reverse()       # ["web02", "web01", "db01"]
```
`in` checks whether a value exists in a list. Returns `True` or `False`.
```python
print("web01" in servers)   # True
print("web99" in servers)   # False
```

## Slicing
Slicing extracts a portion of a list using `[start:stop]`. Start is included, stop is excluded, the same rule as `range()`.

```python
servers = ["web01", "web02", "db01", "db02"]
print(servers[0:2])     # ["web01", "web02"]
print(servers[1:3])     # ["web02", "db01"]
```
Leaving start or stop blank defaults to the beginning or end of the list.
```python
print(servers[:2])      # ["web01", "web02"]
print(servers[2:])      # ["db01", "db02"]
```

## Looping Over a List
You can loop directly over a list with a `for` loop, no index needed.

```python
for server in servers:
    print(server)
```
If you need the index as well, use `enumerate()`.
```python
for index, server in enumerate(servers):
    print(index, server)    # 0 web01
                            # 1 web02