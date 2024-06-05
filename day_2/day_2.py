print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

tippedBill = round((float(bill) * float("1." + tip)) / int(people), 2)

print (f"Each person should pay: ${tippedBill}")