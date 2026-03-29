age = int(input("How old are you? "))           # int() converts the string from input() to an integer so we can compare it numerically
has_id = input("Do you have ID (yes/no)? ")     # input() returns a string, we compare it directly with == "yes"

if age >= 18 and has_id == "yes":               # both conditions must be True and requires all parts to pass
    print("Access granted")
elif age >= 18 and has_id == "no":              # age passes but ID fails, elif only runs if the if above was False
    print("Age is fine but ID is needed")
elif age < 18:                                  # catches anyone under 18 regardless of ID
    print("Too young, no access")
else:                                           # fallback, runs if none of the conditions above were matched
    print("Error try again")