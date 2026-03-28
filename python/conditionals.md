## Conditionals 
Conditionals are a way to govern when code runs or not and which parts of it run. Used to control the code based on if certain conditions are met.

For example:
```python
age = int(input("How old are you? "))
has_id = input("Do you have ID (yes/no)? ")

if age >= 18 and has_id == "yes":
    print("Access granted")
elif age >= 18 and has_id == "no":
    print("Age is fine but ID is needed")
```

## If/else
If/else is a conditional where if 'x' condition is met then run 'y'. Else is used if 'x' isn't fulfilled.

## Elif
Elif lets you check a second condition if the first is False. It's chained decision making.
```python
age = 2
if age == 2:
    print("2")
elif age == 3:
    print("3")
```

## Comparison Operators.
```python
==    # equal to
!=    # not equal to
>     # greater than
<     # less than
>=    # greater than or equal to
<=    # less than or equal to
```
## = and == 
'=' is used to assign a value to a variable. '==' is used to check if 'x' is the same as 'y'.

## Logical Operators 
'and' is used to check if x 'and' y conditions are both met.
```python
if age == 2 and has_id == 'yes': # Checks if BOTH conditions are met
    print("Access granted")
```
'or' is used to check if x 'or' y conditions are met (one or the other).
```python
if age == 2 or has_id == 'yes':  # Check if EITHER condition is met
    print("Access granted")
```
'not' is used to check if 'not' x conditions are met('not True' returns false)
```python
if not has_id: # True if has_id is empty or False
    print("No ID") 
```

