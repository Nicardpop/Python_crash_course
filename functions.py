# Chapter 8 :
	# Functions :
# Defining a Function : 

def greet_user() :# function body :
	# display a simple greeting :
	print("Hello! ")
# calling the function :
greet_user()

# Passing information to a function :

def greet_user(username):# function needs a value for username to work .
	print(f"Hello, {username.title()}! ")

greet_user('jesse')# 'jesse' is an argument .

# Try is yourself :
 # message :
def display_message() :
	print("In this chapter we're learning about functions! ")

display_message()

 # favorite books :
def favorite_books(title) :
	print(f"One of my favorite books is {title.title()}.")


favorite_books('alice in wonderland')

#end;

# Passing arguments :
 # Positinal arguments :
def describe_pet(animal_type,pet_name) :
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','stephan')# we provide the values in order .

# Multiple function calls :

describe_pet('dog','willie') 

describe_pet('harry','hamster')

# key word arguments :

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')


# default values :
def describe_pet(pet_name,animal_type='dog'):
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='harry')
describe_pet(pet_name='barry',animal_type='hamster')

def hi(hello,today):
	print(f"hello {hello}")

# try it yourself :

# T-shirt :
def make_shirt(size,text):
	print(f"\nThe size of the shirt is: {size.title()}")
	print(f"The message on the shirt is: {text.upper()}")
# using order :
make_shirt('m','hello world')
# using keys arguments :
make_shirt(size='m',text='hello world')

# large shirts :

def large_shirts(sizee='l',txt='i love python!'):
	print(f"\nThe size of the shirt is: {sizee.title()}")
	print(f"The message on the shirt is: {txt.upper()}")

large_shirts('l')
large_shirts('m')
large_shirts('s','i love programming!')

# cities :

def describe_city(city,country='usa'):
	print(f"\n{city.title()} is in {country.title()}. ")

describe_city('new york')
describe_city('la')
describe_city('alger','algeria')

# returning a simple value :

def get_formatted_name(first_name,last_name):
	full_name=f"{first_name} {last_name}"
	# the return value :
	return full_name.title()

sam = get_formatted_name('nicard','pop')
print("\n"+sam)

# making an argument optional :

def get_formatted_name(first_name,last_name,middle_name=''):
	if middle_name :
		full_name = f"{first_name} {middle_name} {last_name}"
	else :
		full_name = f"{first_name} {last_name}"
	return full_name.title()

amil = get_formatted_name('hamid','bodb')
print(amil)
sam = get_formatted_name('hac','nicard','pop')
print(sam)

# returning a dictionary :







































