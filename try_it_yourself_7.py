# TRY IT YOURSELF :

# people :
person_0={
	'first_name':'Nicard',
	'last_name':'ben',
	'age':21,
	'city':'BBA',
}
person_1={
	'first_name':'mouh',
	'last_name':'pablo',
	'age':20,
	'city':'BBA',
}
person_2={
	'first_name':'chocho',
	'last_name':'rodolfo',
	'age':20,
	'city':'BBA',
}

people=[person_0,person_1,person_2]

for person in people :
	print(f"\tThe full name: {person['first_name'].title()} {person['last_name'].title()}")
	print(f"\tThe age : {person['age']} years.")
	print(f"\tThe city : {person['city']}")
print()
# pets :
pet_0={'animal_kind':'cat','owner':'john'}
pet_1={'animal_kind':'dog','owner':'marry'}

pets=[pet_1,pet_0]

for pet in pets :
	print(f"The kind of the animal is a {pet['animal_kind'].title()}"
		f" and the owner is {pet['owner'].title()}. ")

print()

# favorite places :

favorite_places={
	'john':['france','marrocco','algerie'],
	'marry':['london','germeny'],
	'sarah':['LA','tunisia']
	}

for names,places in favorite_places.items() :
	print(f"{names.title()}'s favorite places : ")
	for place in places :
		print("\t" + place.title()) 
print()

# favorite numbers :

favorite_numbers= {
	'pablo': [0,1,2] ,
	'peppino': [7,8,9] ,
	'juan': [5,6,4] ,
	'rodolfo': [7,3],
}

for n,numbers in favorite_numbers.items() :
	print(f"\n{n.title()}'s favorite numbers are : ")
	for number in numbers :
		print(f"\t{number}")
print()

# cities :

cities={
	'london':{
		'country':'UK',
		'population':8.6 ,
		'fact':'captil of the world!'
	},
	'new york':{
		'country':'USA',
		'population':8.4 ,
		'fact':'more than 800 language spoken there!'
	},
	'scotland':{
		'country':'UK',
		'population':5.4,
		'fact':'scotland is home to the largest tree in Europe!'
	}
}
for city,city_info in cities.items():
	print(f"\nSome informations about the city of {city.title()}: ")
	print(f"\tThe country: {city_info['country']}")
	print(f"\tThe population: {city_info['population']} million")
	print(f"\tOne fact: {city_info['fact']} ")	

print() 
# extensions :

# end chapter 6 .




 #END ;




















