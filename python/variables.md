## Variables
A variable is a named container that stores a value.

## Data Types
Integer = An integer is a whole number. Typically used for full values such as age, time, etc.

```python
1   4   12  1421
```

Float = A float is a number with a decimal. Usually for numbers that aren't whole. Height, currency, etc.

```python
3.14    12.42   25.14123
```

String = A string is a collection of values in a '' or "", usually for names, passwords, etc.

```python
'hello'     '41'    'hello'     '3.12'      'true'
```

Boolean = A boolean is a value that is either True or False. Used in conditions and  comparisons.

```python
True    False   0   1
```
## input()
Input() is a way to interact with the user. It captures raw text. Even if you type a number '22' it'd take it as a string. Often for if you need to do maths with the value, you need to convert it first.

```python
name = input("What's your name? ")
```
## f-strings
f-strings are strings that allow variables to be embedded within it.

```python
print(f"hey {name}")
```
## Type Conversion
Type conversions are usually used when you want to change a value from one type to another. For example if asking for age using input.

int() converts a value to an integer.

```python
age = int(input("How old are you? "))
```

float() converts a value to a float

```python
currency = float(input("How much USD do you have? "))
```
