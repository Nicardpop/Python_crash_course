# Nesting :

# A list of dictionaries :

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_2,alien_1,alien_0]

for alien in aliens :
	print(alien)

# making an empty list to store aliens :

aliens=[] 

# making 30 green aliens :
for aliens_number in range(30) :# we use range() to repeat the loop 30 time :
	new_value= {'color':'green','points': 5 ,'speed':'slow'}
	aliens.append(new_value)# using append() to add values to the list 
# printing 5 aliens :
for alien in aliens[:5]:
	print(alien)
print('...')
# printing the length of aliens list using len():
print(f'Total number of aliens is :{len(aliens)}.')


for alien in aliens[:3]:
	if alien['color']== 'green' :
		alien['color'] = 'yellow'
		alien['points'] =10
		alien['speed'] ='medium'
	elif alien['color']=='yellow' :
		alien['color'] ='red'
		alien['points'] =15
		alien['speed'] ='fast'

for alien in aliens[:5] :
	print(alien)


# A list in a Dictionary :

pizza ={'crust':'thick','topping':['mushrooms','extra cheese']}

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings :")# we can break the line but we use the ' "..." ' .

for topping in pizza['topping'] :
	print("\t"+topping)

favorite_language ={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell']
}

for name, languages in favorite_language.items() :
	if len(languages) > 1 :
		print(f"\n{name.title()}'s favorite languages are :")
		for language in languages :
			print(f'\t{language.title()}')
	else :
		print(f"\n{name.title()}'s favorite language is :")
		for language in languages :
			print(f'\t{language.title()}')
		

# Dictionary in a Dictionary :

users={
	'einstein':{
		'first':'albert',
		'last':'einstein',
		'location':'pinceton',

	},
	'mcurie':{
		'first':'marie'
		,'last':'curie',
		'location':'paris',
	}
}

for user,user_info in users.items() :
	print(f"\nUsername :{user.title()}")
	full_name=f"{user_info['first']} {user_info['last']}"
	location=user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
