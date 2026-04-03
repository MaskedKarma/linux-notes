# With 1 function.

def calculator(bill, percentage, group):        # Single function that calculates tip, total and share.
    while group == 0:
        print("Sorry, please try again.")
        group = int(input("How large is your party? "))
    
    tip = bill * (percentage / 100)
    total = bill + tip
    share = total / group
    print(f"Tip:              £{tip:.2f}")
    print(f"Total bill:       £{total:.2f}")
    print(f"Each person owes: £{share:.2f}")

bill = float(input("What's your bill? "))
percentage = float(input("How much are you tipping? "))
group = int(input("How large is your party? "))

calculator(bill, percentage, group)

# With functions for each part.

def calculate_tip(bill, percentage):        # Function that calculates tip
    tip = bill * (percentage / 100)
    return tip


def calculate_total(bill, tip):             # Function that calculates total
    total = bill + tip
    return total


def split_bill(total, people):              # Function that calculates share
    while people == 0:
        print("Sorry, please try again.")
        people = int(input("How many people are dining with? "))
    share = total / people
    return share

bill = float(input("What's your bill? "))
percentage = float(input("What percent would you like to tip? "))
people = int(input("How many people are you dining with? "))

tip = calculate_tip(bill, percentage)
total = calculate_total(bill, tip)
share = split_bill(total, people)

print(f"Tip:              £{tip:.2f}")
print(f"Total bill:       £{total:.2f}")
print(f"Each person owes: £{share:.2f}")
