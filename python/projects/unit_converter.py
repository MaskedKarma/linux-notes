# Final Code

# Unit converter for Length, weight and temperature
import time

def length(km):          # Km to Miles conversion
    final_miles = km * 0.621371
    return final_miles

def length2(miles):         # Miles to Km conversion
    final_km = miles * 1.60934
    return final_km

def weight(kg):            # Kg to Lbs conversion
    final_lbs = kg * 2.20462
    return final_lbs

def weight2(lbs):           # Lbs to Kg conversion
    final_kg = lbs * 0.453592
    return final_kg

def temperature(c):          # Celcius to Fahrenheit conversion
    final_f = (c * 9/5) + 32
    return final_f

def temperature2(f):         # Fahrenheit to Celcius
    final_c = (f - 32) * 5/9
    return final_c 

print("Hello Welcome to Unit Calculator!")
print()
print()
print("Please type the number for your unit!")
attempts = 0
while True:
    key = int(input("1. Length  2. Weight   3. Temperature  4. Quit "))
    while key not in (1, 2, 3, 4):
        attempts += 1
        if attempts >= 5:
            print()
            print()
            print("Too many invalid attempts. Goodbye!")
            exit()
        time.sleep(1)
        print("Sorry please type a number corresponding to one of our units! :)")
        key = int(input("1. Length  2. Weight   3. Temperature  4. Quit "))

    if key == 4:
        print()
        print()
        print("Thank you for using us! Goodbye!")
        break

    elif key == 1:
        print("You've chosen length!")
        print()
        print()
        print("Which length would you like to convert?")
        length_call = int(input("1. Convert Km to Miles     2. Convert Miles to Km     3. Go back  "))
        while length_call not in (1, 2, 3):
            print("Sorry! That's not one of our options, please try again!")
            attempts += 1
            if attempts >= 5:
                print()
                print()
                print("Too many invalid attempts. Goodbye!")
                exit()
            time.sleep(1)
            length_call = int(input("1. Convert Km to Miles     2. Convert Miles to Km     3. Go back   "))
        if length_call == 1:
            km = float(input("How many Kilometres would you like to convert?  "))
            miles = length(km)
            print(f"You are left with {miles:.2f} miles.")
        elif length_call == 2:
            miles = float(input("How many Miles would you like to convert?    "))
            km = float(length2(miles))
            print(f"You are left with {km:.2f} kilometres.")
        elif length_call == 3:
            continue
        
    elif key == 2:
        print("You've chosen Weight!")
        print()
        print()
        print("Which weight would you like to convert?")
        weight_call = int(input("1. Convert kg to lbs   2. Convert lbs to kg    3. Go back  "))
        while weight_call not in (1, 2, 3):
            print("Sorry! That's not one of our options, please try again!")
            attempts += 1
            if attempts >= 5:
                print()
                print()
                print("Too many invalid attempts. Goodbye!")
                exit()
            time.sleep(1)
            weight_call = int(input("1. Convert kg to lbs   2. Convert lbs to kg    3. Go back  "))
        if weight_call == 1:
            kg = float(input("How many Kilograms are you converting?    "))
            lbs = weight(kg)
            print(f"You are left with {lbs:0.2f} pounds.")
        elif weight_call == 2:
            lbs = float(input("How many pounds are you converting?  "))
            kg = weight2(lbs)
            print(f"You are left with {kg:0.2f} kilograms.")
        elif weight_call == 3:
            continue
    elif key == 3:
        print("You've chosen Temperature!")
        print()
        print()
        print("Which temperature are you converting from?")
        temp_call = int(input("1. Convert from c to f  2. Convert from f to c   3. Go back   "))
        while temp_call not in (1, 2, 3):
            print("Sorry! That's not one of our options, please try again!")
            attempts += 1
            if attempts >= 5:
                print()
                print()
                print("Too many invalid attempts. Goodbye!")
                exit()
            time.sleep(1)
            temp_call = int(input("1. Convert from c to f   2. Convert from f to c  3. Go back   "))
        if temp_call == 1:
            c = float(input("What is the Celcius? "))
            f = temperature(c) 
            print(f"The fahrenheit is {f:.2f}!")
        elif temp_call == 2:
            f = float(input("What is the fahrenheit?  "))
            c = temperature2(f)
            print(f"The celcius is {c:.2f}!")
        elif temp_call == 3:
            continue

