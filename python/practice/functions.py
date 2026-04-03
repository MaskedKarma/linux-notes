# Function does the work
def square(num):
    return num * num        # returns num multiplied by itself, the result is passed back to the caller

# Caller handles input and output
num = int(input("Give a number please: "))      # int() wraps input() because input() always returns a string, we need a number
print(square(num))      # passes num into the function, prints whatever it returns

def is_even(num):
    return num % 2 == 0     # % is modulo (remainder after division), if remainder is 0 the number divides evenly by 2
                            # num % 2 == 0 is a comparison that returns True or False, we return that boolean directly

num_even = int(input("Give me a number: "))     # same pattern — convert input to int before passing to the function
print(is_even(num_even))        # prints True or False depending on what is_even() returns


def greet_user(language, name):      # two parameters — the function needs both pieces of info to do its job
    
    if language == "spanish":
        print(f"Hola, {name}")
    elif language == "russian":
        print(f"Bvyet, {name}")
    elif language == "japanese":
        print(f"Konichiwa, {name}")
    elif language == "english":
        print(f"Hello, {name}")
    else:
        print(f"Sorry, '{language}' isn't supported yet.")
language = input("What Language would you like? ").lower()      # .lower() normalises the input so "Spanish" and "SPANISH" both match "spanish"
name = input("What's your name? ")
greet_user(language, name)