# CAPSTONE PROJECT 1
# Compulsory Task 1

# This program wil consist of a finance calculator
# The user can chosse between
# calculating either interest on an investment
# or the monthly homeloan repayment amoount

# Importing relevant modules
import math

# Underlined Heading
print("\x1B[4m" + "Calculator Options:" + "\x1B[0m")

# Requesting input from user: Calculator Option
calc = input("""
investment      - to calculate the amount of interest you'll earn on your investment
bond            - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()


i = 0
while i == 0:

    # Investment Calculator
    if calc == "i" or calc == "invest" or calc == "investment":
        p = float(input("Enter deposit amount (ZAR): R "))
        r = float(input("Enter desired interest rate in % (numbers only): "))
        t = int(input("Enter investment duration in years: "))
        interest = input("""
\x1B[4mInterest Options:\x1B[0m
    
s               - simple interest
c               - compound interes
    
Enter option here: """).lower()

        j = 0
        while j == 0:

            if interest == "s" or interest == "simple":
                a = p * (1 + (r/100) * t)
                j = 1

            elif interest == "c" or interest == "compound":
                a = p * math.pow((1 + (r/100)), t)
                j = 1

            else:
                interest = input("""\nUnknown input, please try again:        
s               - simple interest
c               - compound interes
    
Enter either 's' or 'c': """).lower()

        # Output
        print(f"If you deposit an amount of R {p:,.2f}, the amount with interest you will have earned after {t} years will be R {a:,.2f}.")

        # Exiting loop
        i = 1


    # Bond Calculator
    elif calc == "b" or calc == "bond":
        p = float(input("Enter the selling price of the house (ZAR): R "))
        i = float(input("Enter the current interest rate for mortgage loans in % (numbers only): "))
        n = int(input("Enter desired repayment period in months: "))
        repayment = (((i/100) / 12) * p) / (1 - (1 + ((i/100) / 12))**(-n))

        # Output
        print(f"Your monthly mortgage repayment will be R {repayment:,.2f} per month.")

        # Exiting loop
        i = 1


    # Error message for unknown input
    else:
        calc = input("""\nUnknown input, please try again:        
investment      - to calculate the amount of interest you'll earn on your investment
bond            - to calculate the amount you'll have to pay on a home loan
    
Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()