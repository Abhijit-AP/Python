# to print the length of integer or numbers print(len(str(12345)))
# to print the character based on index number print("Hello"[0])
num_char = len(input("What is your name? "))
print("your name has " + str(num_char) + " characters")
# always convert integers to string before printing

user_input = input("Enter a two digit number to add: ")
num1 = int(user_input[0])
num2 = int(user_input[1])
print(num1+num2)


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = int((weight / (height * height)))
# you can also use height ** 2
print(bmi)

# f-string
score = 0
height = 1.82
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# exercise to calculate life left
age = int(input("What is your current age? "))
days = 90 * 365
weeks = 90 * 52
months = 90 * 12

user_days = age * 365
user_weeks = age * 52
user_months = age * 12

days_left = days - user_days
weeks_left = weeks - user_weeks
months_left = months - user_months

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left")

# exercise to create a tip calculator
amount = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to splut the bill? "))

bill_perPerson = round((amount + (amount * tip / 100)) / people, 2)
toPay = "{:.2f}".format(bill_perPerson)

print(f"Each person should pay: ${toPay}")

# the round function sometimes does not output the exact numbers
# this is a formatting issue
# use the function "{:.2f}".format(variable_name) to get the format correct
