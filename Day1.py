# print("Hello to you too")
# print("Hello there \nHello there \nHello there")
# print("Hello " + "Angela")

# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the '+' sign.")
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

print("Hello " + input("What is your name?: "))
# the above first prompts for input and then prints the message

print(len(input("What is your name?: ")))
# the above first prompts for the input and then prints the length of the input.

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a = "+a)
print("b = "+b)

print("Welcome to the Band name generator.")
city = input("What was the city you grew up in? ")
pet = input("What is your pet name? ")
print("Your band name should be " + city + " " + pet)
