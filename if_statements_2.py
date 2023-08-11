# if - elif -else :
# if :
age = 19 
if age >= 18 :
	print("Your are old enough to vote !")
	print("Have you registered to vote yet? ")
# the condition test pass , and both print() are indented ^

# else :

else :
	print("Sorry,but you're to young to vote .")
	print("please registered to vote as soon as you turn 18!")
# when the first condition fail , the else both print() are indented 
# NOTE : the if_else works well in situation in which your have to possible actions to evaluate .

# IF_ELIF_ELSE :

# amusement_park.py:

age = 12 
if age <4 :
	price = 0
elif age <18 :# we can use as many as elif blocks as we want :
	price= 25
elif age < 65 :
	price = 40
else :
	price = 20

print(f"Your admission cost is ${price}")

# the elif indente only when if fail .
print("\n\n")
 
 # we can use only if :"
requested_topping = ["mushrooms","extra cheese"]

if "mushrooms" in requested_topping :
	print("adding mushrooms")
if "pepperoni" in requested_topping :
	print("\nadding pepperoni topping")
if "extra cheese" in requested_topping :
	print("\nadding extra cheese ")
# this code would not work properly if we used the if_elif_else chaine .


# Try_it_yourself :
# Alien colors :
Alien_Colors=['green','red','yellow']

if 'green' in Alien_Colors :
	print("The player just earned 5 points!")
elif 'blue' in Alien_Colors :
	print()

print("\n\n")
Alien_color= 'green'
if Alien_color == 'green' :
	print("You just earned 5 points!")
elif Alien_color == 'yellow' :
	print("You just earned 10 points!")
else :# alien red :
	print("You just earned 15 points!")

print("\n\n")

# stages of life :
age = 5 

if age < 2 :
	print("This person is a baby .") 
elif age >= 2 and age < 4 :
	print("This person is a toddler .")
elif age >=4 and age < 13 :
	print("This person is a kid .")
elif age >=13 and age < 20 :
	print("This person is a teenager .")
elif age >=20 and age <65 :
	print("This person is a adult .")
else :
	print("This person is an elder .")
  
print("\n\n")
# fruit list :

fruits =['banana','orange','apple','mango','avocado']

if 'banana' in fruits :
	print("I really love bananas! ")
if 'orange' in fruits :
	print("\nI really love oranges! ")
if 'apple' in fruits :
	print("\nI really love apples! ")
if 'mango' in fruits :
	print("\nI really love mangos! ")
if 'avocado' in fruits :
	fruit='avocado'

print(f"\nI really like{fruit}s")

# end ;

print("\n\n")

# working with lists and if statments :

requested_toppings = ['mushrooms','green_peppers','extra_cheese']

for requested_topping in requested_toppings :
	if requested_topping == 'green_peppers' :
		print("\nSorry we are out of green pappers !")
	else :
		print(f"\nAdding the {requested_topping}")

print("\nYour pizza is ready !")
print("\n\n")
# checking if a list is empty :
requested_toppings=[]

# we use name of the list in an if statement to verify if its empty by returning true of false : 
if requested_toppings :
	for requested_topping in requested_toppings :
		print(f"adding {requested_topping}. ")
	print("\nYour pizza is ready. ")
else :
	print("Are you sure you want a plain pizza? ")

print('\n\n')
# using multiple lists :
available_toppings = ['mushrooms','green_peppers','extra_cheese','olives']

requested_toppings= ['mushrooms','french fries','extra_cheese']

for requested_topping in requested_toppings :
	if requested_topping in available_toppings :
		print(f"adding {requested_topping}.")
	else:
		print(f"Sorry , but we dont have {requested_topping} .")
print("\nYour pizza is ready. ")










