# Welcome Statement
print("Welcome to the Tip Calculator.")

# User Inputs
amount_owed = input("Enter the Total Bill: R")
percentage_tip = input("What percentage tip would you like to give? 10, 12, 15: ")
num_people = input("Enter how many people will split the bill: ")

# Calculation
amount_per_person = float(amount_owed) / 100 * (int(percentage_tip) + 100) / int(num_people)

# Final Output
print(f"Each person should pay R{round(amount_per_person, 2)}")
