# if else conditions and treasure island game

print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")

# second exercise to check even and odd number

number = int(input("Which number do you want to check? "))
num = number % 2
if num == 0:
    print("Its an even number")
else:
    print("Its an odd number")

# third exercise to practice elif

height = int(input("What is your height in cm ?"))

if height >= 120:
    age = int(input("What is your age? "))
    if age > 18:
        print("You can ride the rollercoaster by paying $12")
    elif age < 12:
        print("You can ride the rollercoaster by paying $5")
    else:
        print("You can ride the rollercoaster by paying $7")
else:
    print("You have to grow a little to ride the rollercoaster")

# fourth exercise on BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round((weight / (height * height)), 0)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and are obese")
else:
    print(f"Your BMI is {bmi} and are clinically obese")

# identifying a leap year

yearInput = int(input("Enter the year to check for leap year: "))
if yearInput % 4 == 0 and yearInput % 100 == 0 and yearInput % 400 == 0:
    print("This is a leap year")
elif yearInput % 4 == 0 and yearInput % 100 == 0 and yearInput % 400 != 0:
    print("This is not a leap year")
elif yearInput % 4 == 0 and yearInput % 100 != 0:
    print("This is a leap year")
else:
    print("This is not a leap year")

# other way of doing the leap year exercise

yearInput = int(input("Enter the year to check for leap year: "))

if yearInput % 4 == 0:
    if yearInput % 100 == 0:
        if yearInput % 400 == 0:
            print("This is a leap year")
        else:
            print("Not a leap year")
    else:
        print("This is a leap year")
else:
    print("Not a leap year")

# multiple IF statements.

height = int(input("What is your height in cm? "))
bill = 0

if height < 120:
    print("You cannot ride the rollercoaster")
elif height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Children ticket is $5")
    elif age < 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")

    pic = input("Do you want a picture? Y or N: ")

    # Here is the multi IF statement
    if pic.upper() == "Y":
        bill += 3
        print(f"Your total bill is ${bill}")
    elif pic.upper() != "N":
        pic = input("Invalid input, please type Y or N: ")
    if pic.upper() == "Y":
        bill += 3
        print(f"Your total bill is ${bill}")
    elif pic.upper() != "N":
        print("Invalid input, exiting... please restart transaction")

# Pizza ordering application.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

cost = 0

if size.upper() == "S":
    cost = 15
if size.upper() == "M":
    cost = 20
if size.upper() == "L":
    cost = 25

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        cost += 2
    else:
        cost += 3

if extra_cheese.upper() == "Y":
    cost += 1

print(f"Total cost of Pizza is ${cost}")

# Love calculator application

print("Welcome to the love calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_name = name1 + name2

true_count = combined_name.count("t") + combined_name.count("r") \
             + combined_name.count("u") + combined_name.count("e")
love_count = combined_name.count("l") + combined_name.count("o") \
             + combined_name.count("v") + combined_name.count("e")

tmp_score = str(true_count) + str(love_count)
score = int(tmp_score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

# Treasure Island application

print("Welcome to the treasure island game!")
print("To find the treasure, first, you will have to choose a path")

path = input("Which path do you choose to go? left or right? \n")
if path.lower() != "left":
    print("Game over!")
else:
    print("You have chose correctly, but there is a river to cross!")
    cross = input("Do you want to swim or wait? \n")
    if cross.lower() != "wait":
        print("Game over!")
    else:
        print("You have chosen correctly, you come across 3 doors which are red, blue and yellow")
        door = input("Which door do you choose to enter? \n")
        if door.lower() != "yellow":
            print("Game over!")
        else:
            print("You win!")