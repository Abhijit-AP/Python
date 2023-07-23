# PyPassword Generator

import passchar
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

li = []

if nr_letters > 0:
    for num in range(0, nr_letters):
        li.append((random.choice(passchar.letters)))
if nr_symbols > 0:
    for num in range(0, nr_symbols):
        li.append((random.choice(passchar.symbols)))
if nr_numbers > 0:
    for num in range(0, nr_numbers):
        li.append((random.choice(passchar.numbers)))

# instead of append, you can also use li += random.choice(passchar.numbers)
# similarly you can do this for getting a string instead of a list

random.shuffle(li)

password = ""
for num in li:
    password += num

print(password)
