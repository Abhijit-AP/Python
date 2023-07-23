# coin toss exercise
import random

cointoss = random.randint(0, 1)
if cointoss == 1:
    print("heads")
else:
    print("tails")

# Name picker

import random

name_string = input("Give me everybody's name, separated by a comma. ")
names = name_string.split(", ")
rand = random.randint(0, len(names) - 1)
print(f"{names[rand]} is going to buy the food today")

# Another way to use random class is to use the .choice function

import random

name_string = input("Give me everybody's name, separated by a comma. ")
names = name_string.split(", ")
# rand = random.randint(0, len(names)-1)
print(f"{random.choice(names)} is going to buy the food today")

# Treasure map exercise

row1 = ["😁", "😁", "😁"]
row2 = ["😁", "😁", "😁"]
row3 = ["😁", "😁", "😁"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Column# and Row#: ")
col = int(position[0])
row = int(position[1])
selected_row = map[row - 1]
selected_row[col - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# Easier way of writing the above code using matrix style i.e map[0][2]

row1 = ["😁", "😁", "😁"]
row2 = ["😁", "😁", "😁"]
row3 = ["😁", "😁", "😁"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Row# and Column#: ")
row = int(position[0])
col = int(position[1])
map[row - 1][col - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# Even easier is to pass the calculations directly in the reassigning statement

row1 = ["😁", "😁", "😁"]
row2 = ["😁", "😁", "😁"]
row3 = ["😁", "😁", "😁"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Row# and Column#: ")
map[int(position[0]) - 1][int(position[1]) - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# rock paper scissor game

import rps
import random

print("Welcome to the Rock Paper Scissors game!")
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: ")

if int(choice) != [0, 1, 2]:
    print("Invalid choice")
    exit()

selection = [rps.rock, rps.paper, rps.scissors]
user_selection = selection[int(choice)]
comp_selection = random.choice(selection)
print(f"You chose:\n {user_selection}")
print(f"Computer chose:\n {comp_selection}")

if user_selection == rps.rock:
    if comp_selection == rps.paper:
        print("You Lose")
    elif comp_selection == rps.rock:
        print("Draw")
    else:
        print("You Win")

if user_selection == rps.paper:
    if comp_selection == rps.paper:
        print("Draw")
    elif comp_selection == rps.rock:
        print("You Win")
    else:
        print("You Lose")

if user_selection == rps.scissors:
    if comp_selection == rps.paper:
        print("You Win")
    elif comp_selection == rps.rock:
        print("You Lose")
    else:
        print("Draw")