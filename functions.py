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

def build_person(first_name ,last_name,age=None):
  person = {'first': first_name,'last':last_name}     
  if age:
    person['age'] = age

  return person

mus = build_person('danyl','karboub',age=23)
print(mus)

# Using a function with a while loop :

def get_formate_name_1(first_name,last_name):
  fullname = f"{first_name} {last_name}"
  return fullname.title()

while True:
  print("\nPlease tell me your name:\n")
  f_n = input("first name :")
  l_n = input("last name :")

  formatted_name_1 = get_formate_name_1(f_n,l_n)


  print(f"\nHello, {formatted_name_1}")


# Passing a List :
def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = f"Hello ,{name.title()}!"
    print(msg)


usernames = ['danyl','nicard','ty']
greet_users(usernames)


# modifying a List in a Function :

unprinted_designs = ['robot','case','phone case']

completed_designs = []


while unprinted_designs :
  current_design = unprinted_designs.pop()
  print(f"Printing Model:{current_design}")
  completed_designs.append(current_design)


print("this are all the completed designs :\n")

for comp in completed_designs:
  print(f" - {comp}")

# optimize the program above using funcitnos :

unprinted_models_1 = ['case','phone','cup']


def print_models(unprinted_models_1,completed_models_1):
  while unprinted_models_1 :
    current_design = unprinted_models_1.pop()
    print(f"Printing Model :{current_design}")
    completed_models_1.append(current_design)

def print_completed(completed):
  print("\nthis are the completed models:\n")
  for comp in completed :
    print(f" - {comp}")


completed_models_1 = []

print_models(unprinted_models_1,completed_models_1)
print_completed(completed_models_1)



# passing on  Arbitrary NUmber of arguments;


def make_pizza(*toppings):
  print("\nMaking a pizza with the following toppings :")
  for topping in toppings :
    print(f" - {topping}")
    
make_pizza('pepperoni')

make_pizza('mushrooms','green pepper','extra cheese')


# using arbitrary  keyword arguments :

def build_profile_1(first, last ,**user_info):
  user_info['first_n'] = first
  user_info['last_n'] = last 
  return user_info

user_profile = build_profile_1('danyl', 'kerboub',location='algeria',gender='male')

print(user_profile)

# try it yourself :

def sandwich_order(*ingredients):
  print("\nsandwich ingredients :")
  for ingre in ingredients :
    print(f" - {ingre}")

sandwich_order('fries','onions','cheese')


# # importing an entire module :

# import pizza 

# pizza.make_pizza(12,'cheese')


# importing a function from a module :

from pizza import printing_hello as ph 

ph() #function says hello !












