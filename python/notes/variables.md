# Variables

## Variables
A variable is a named container that stores a value.

```python
name = "Adam"
age = 25
```

## Data Types
Integer = A whole number. Used for countable values like age, quantity, time.

```python
1   4   12   1421
```
Float = A number with a decimal. Used for values that aren't whole like height or currency.

```python
3.14    12.42   25.14123
```
String = A sequence of characters in `''` or `""`. Used for names, messages, passwords.

```python
'hello'     '41'    'hello world'     '3.12'
```
Boolean = A value that is either `True` or `False`. Used in conditions and comparisons.

```python
True    False
```

## input()
`input()` captures text from the user as a string. Even if you type a number it comes back as a string — convert it first if you need to do maths with it.

```python
name = input("What's your name? ")
```

## f-strings
f-strings let you embed variables directly inside a string.

```python
print(f"Hey {name}")
```

## Type Conversion
Type conversion changes a value from one type to another. Commonly used when taking input and needing a number.

`int()` converts a value to an integer.

```python
age = int(input("How old are you? "))
```
`float()` converts a value to a float.

```python
currency = float(input("How much USD do you have? "))
```
`str()` converts a value to a string.

```python
message = "You are " + str(age) + " years old"
```

## .lower()
`.lower()` converts a string to lowercase. Used on input to make comparisons reliable regardless of how the user typed it.

```python
language = input("What language? ").lower()
```