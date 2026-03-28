age = int(input("How old are you? "))
has_id = input("Do you have ID (yes/no)? ")

if age >= 18 and has_id == "yes":
    print("Access granted")
elif age >= 18 and has_id == "no":
    print("Age is fine but ID is needed")
elif age < 18: 
    print("Too young, no access")
else: 
    print("Error try again")


