# Chapter 7 :

# The input() function :
"""
message=input("Tell me something, and I will repeat it back to you :")
print(message)

name=input("Please enter your name : ")
print(f"\nHello, {name}!")

prompt="If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your name? "
name =input(prompt) 
print(f"\nHello, {name}!")

# using int() to accept numerical unput :
age = input("How old are you? ")
print(age)# this number is a string we cant use it as a number or we'll get an error !

# we ise int() :
# we convert the input value to a numerical representation :
age = int(age)  
print(age>=18)# the output is true !

height=input("How tall are you, in inches?") 
height=int(height)

if height >= 48 :
	print("\nYou are tall enough to ride! ")
else :
	print("\nYou will be able to ride when you're little older. ")


# The modulo operator :

number =input("Enter a number, and I'll tell you if it's even or odd: ")
number= int(number)

if number % 2 == 0 :
	print(f"\nThe number {number} is even! ")
else:
	print(f"\nThe number {number} is odd! ")
"""
# Try it yourself :

# rental car :
car = input("What kind of car you would like to rent? ")
print(f"Let me see if I can find you a {car}")

# restaurant seating :

people = input("How many people are in your dinner group? ")
people=int(people)

if people > 8 :
	print("\nYou will have to wait for a table. ")
else :
	print("\nYour table is ready. ")

# multiples of ten :
number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number=int(number) 

if number % 10 == 0 :
	print(f"\nThe number {number} is a multiple of 10!")
else :
	print(f"\nThe number {number} is not a multiple of 10. ")


# end;












