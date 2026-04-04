## Conditionals
Conditionals control which parts of your code run based on whether a condition is met.

## if / elif / else
`if` runs a block when its condition is True. `elif` checks another condition if the one above was False. `else` is the fallback — it runs if nothing above matched.
```python
age = int(input("How old are you? "))
has_id = input("Do you have ID (yes/no)? ")

if age >= 18 and has_id == "yes":
    print("Access granted")
elif age >= 18 and has_id == "no":
    print("Age is fine but ID is needed")
elif age < 18:
    print("Too young")
else:
    print("Something went wrong")
```

## Comparison Operators
```python
==    # equal to
!=    # not equal to
>     # greater than
<     # less than
>=    # greater than or equal to
<=    # less than or equal to
```

## = vs ==
`=` assigns a value to a variable. `==` checks whether two values are equal.
```python
age = 18        # assigns 18 to age
age == 18       # checks if age is equal to 18 — returns True or False
```

## Logical Operators
`and` requires all conditions to be True.
```python
if age >= 18 and has_id == "yes":   # both must pass
    print("Access granted")
```
`or` requires at least one condition to be True.
```python
if age >= 18 or has_id == "yes":    # either one passing is enough
    print("Access granted")
```
`not` inverts a boolean — True becomes False, False becomes True.
```python
if not has_id:                      # True if has_id is empty, False, or None
    print("No ID provided")
```