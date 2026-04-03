name = input("What's your name?  ")             # input() prompts the user and returns their response as a string
age = int(input("How old are you? "))           # int() converts the string returned by input() to an integer
height = float(input("How tall are you in metres?"))        # float() converts the string returned by input() to a float
print(f"{name} is {age} years old and {height} metres tall")        # f-string lets us embed variables directly in the string using {}