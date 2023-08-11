# CHAPTER 6 :

#A simple dictionary :
alien_0 = {'color':'green','point': 5}# this is a dictionary . 
# how we print element of a dictionary :
print(alien_0['color'])
print(alien_0['point'])

#accessing values in a dictionary :
# example :

new_point= alien_0['point']
print(f"\nYou just earned {new_point} points! ")

# Adding new key-value pairs :

print(alien_0)
# this is how we add a new key-value :
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print("The new alien_0 status :")
print(alien_0)

# starting with an empty dictionary :

alien_0 ={}
# adding key-values :
alien_0['color'] = 'green'
alien_0['point'] = 5

print(alien_0)

# modifiying values :

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'

print(f"\nThe alien is now {alien_0['color']}.")

# example :

alien_0 ={'x_position': 0 , 'y_position': 25 ,'speed': 'medium'}

print(f"Original x-position {alien_0['x_position']}")

#moving the alien to the right :

if alien_0['speed'] == 'slow' :
	x_increment = 1 
elif alien_0['speed'] == 'medium' :
	x_increment = 2
else :# alien fast :
	x_increment = 3 
# we change the position :
alien_0['x_position'] =+ x_increment 
# new position :
print(f"New x-position : {alien_0['x_position']}")

# removing key-value pairs :

alien_0 ={'color':'green' , 'point': 5}
# del to remove from the dictionary :
del alien_0['point']

print(alien_0)

# A dictionary of similar Objects :

favorite_language ={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

language=favorite_language['sarah']
print(f"Sarah's favorite language is {language.title()}.")

# using get() to access values :

# using get :

alien_0 = {'color':'green','speed':'medium'}
# the first argument is the name of key-value we're looking for and the second is optional 
# for if the key doesnt existe :
point_value = alien_0.get('points','No point value assigned .')

print(point_value)

# we use get to avoid the error message .

# try it yourself :

# person :

person = {
	'first_name':'nicard',
	'last_name':'juan',
	'age':20,
	'city':'BBA',
}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'])


# favorite number :

favorite_numbers= {'pablo': 0 ,'peppino': 7 ,'juan': 5 ,'rodolfo': 7}

# glossary :

dictionary = {'indent':'add','del':'delete','python':'language','append':'indent','get':'find'}	

print(f"'indent' means ,{dictionary['indent'].title()}. ")
print(f"'del' means , {dictionary['del'].title()}. ")
print(f"'python' , {dictionary['python']} . ")
print(f"'append' , {dictionary['append']}. ")
print(f"'get' , {dictionary['get']}. ")

# end;


user_0 = {
	'username':'efermi',
	'first_name':'enrico',
	'last_name':'fermi',
} 
for key, value in user_0.items() :# we use the method items() to access all key-values in the dic
	print(f"\nkey : {key}")
	print(f"value : {value}")


# example :

for name, language in favorite_language.items() :
	print(f"\nName : {name.title()}")
	print(f"Language : {language.title()}")
print("\n")

# looping through all the keys :
# we use the method keys() :
for name in favorite_language.keys() :# /or\  for name in favorite_language :
	print(name.title())

# the output is : jen sarah edward phil .

friends = ['sarah','phil']
for name in favorite_language :
	print(f"Hi {name.title()}. ")
	if name in friends :
		language = favorite_language[name].title() 
		print(f"\t{name.title()}, I see you love {language}! ")

if 'erin' not in favorite_language.keys() :# we can use keys() method to check the key-values too!
	print("Erin, please take our poll! ")

# looping through a dictionary's keys in a particular order : 

# We use the sorted() function to get a copy of the keys in order :
# using sorted() :
for name in sorted(favorite_language.keys()) :
	print(f"{name.title()}, thank you for taking the poll. ")


# looping through all values :

# we use the values() method :

print("The following languages have been mentioned :")
for language in favorite_language.values() :
	print(language.title()) 
# we get the values without the keys .
print("\n")
# using set() to show only unique items and to avoid duplicate items :

for language in set(favorite_language.values()) :
	print(language.title())
# we avoided the repetition of the word 'python'.
print('\n')
#we can build a set :
language = {'python','ruby','python','c'}# this is a set .
print(language)

# the output : {'ruby','python','c'} .

# try it yourself :

# glossary 2 :

dictionary = {'indent':'add','del':'delete','python':'language','append':'indent','get':'find'}
dictionary['set']='find unique value.'
dictionary['sorted']='order the keys.'
for key, v in dictionary.items():
	print(key.title())
	print(f",{v.title()}. ")


# Rivers :

rivers={'nile':'egypt','wandsbeck':'england','tweed':'scotland'}


for river, country in rivers.items() :
	print(f"The {river.title()} runs through {country.title()}.")

print()
print("The name of the rivers :")
for riv in rivers.keys() :
	print(riv.title())

print()
print("The countries are :")
for count in rivers.values() :
	print(count.title()) 
print()
# polling :
favorite_language ={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
people_list=['sarah','jen','edward','phil','sam','ben','robinson']

for one in people_list :
	if one in favorite_language :
		print(f"{one.title()}, thank you for taking the poll! ")
	else :
		print(f"{one.title()}, please take our poll.")

# end;












