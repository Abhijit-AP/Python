# for loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# while loops
# infinite loop
i = 1
a = 2
while a > i:
    print(a)

# range(0, 3) gives you the range of numbers from 0, 1, 2
# the below converts the string to int in the list
students_heights = input("input heights of students: ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

# average using for loops

students_heights = input("input heights of students: ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
#print(students_heights)

tot = 0

for n in students_heights:
    tot = tot + n

#print(round(tot / len(students_heights)))
print(f"Average is : {round(sum(students_heights)/len(students_heights))}")

# Find the max in the list of numbers

max_number = input("Input numbers to find max: ").split()
for n in range(0, len(max_number)):
    max_number[n] = int(max_number[n])

m = 0
for n in max_number:
    if n > m:
        m = n

print(m)

# Add up 1 to 100

tot = 0
for number in range (1,101):
    tot += number

print(tot)

# adding even numbers

tot = 0
for number in range(1, 101):
    if number%2 == 0:
        tot +=number

print(tot)

# or you can also use

tot = 0
for number in range(2, 101, 2):
    tot += number

print(tot)

# Fizzbuzz game

tot = 0
for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("Fizzbuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)


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

random.shuffle(li)

password = ""
for num in li:
    password += num

print(password)
