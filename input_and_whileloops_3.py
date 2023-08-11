# using while with lists and Dictionaries :

# moving items from one list to another :

# Ex :
# users unconfirmed .
unconfirmed_users = ['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users :
	current_user=unconfirmed_users.pop()

	print(f"\nVerifying user : {current_user.title()}")
	confirmed_users.append(current_user)
print("The following users have been confirmed: ")
for confirmed_user in confirmed_users :
	print(confirmed_user.title())
# users confirmed .
# note : unconfirmed_users is empty .


# Removing all instancees of specific values from a list :

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
# removing all 'cat' from the list :
while 'cat' in pets :
	pets.remove('cat')

print(pets)

# filling a dictionary with user input :

responses={}

polling_active = True 

while polling_active :
	name=input("Please enter your name : ")
	response=input("Which mountain would you like to climb someday: ")
	responses[name]=response
	repeat=input("Would you like to let anotehr person respond? (yes/ no) ")
	if repeat == 'no' :
		polling_active = False 

print("--- polling result ---")
for name,response in responses.items() :
	print(f"{name.title()} would like to climb {response.title()}")












