# Function does the work
def square(num):
    return num * num

# Caller handles input and output
num = int(input("Give a number please: "))
print(square(num))

def is_even(num):
    return num % 2 == 0

num_even = int(input("Give me a number: "))
print(is_even(num_even))

def greet_user(language, name):
    
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
language = input("What Language would you like? ").lower()
name = input("What's your name? ")
greet_user(language, name)