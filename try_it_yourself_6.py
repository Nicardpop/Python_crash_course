#TRY IT YOURSELF 6 :

# Hello admin :

list_users = ['jaden','michel','pablo','admin','mike']

for user in list_users :
	if user == 'admin' :
		print("Hello Admin, would you like to see a status report ?")
	else :
		print(f"Hello {user.title()}, thank you for logging in again !")

print("\n\n")
# No users :

No_users =[]

if No_users :
	for user in No_users :
		print("Hello !")
else :
	print("We need to find some users ")

print('\n\n') 
# checking users names :

current_users=['jaden','melcom','john','darwin','mike']

new_users=['nacim','JADEN','john','mike','DARWIN']


for user in new_users :
	you = user.lower()# to make sure thats used names are not accepted in upper case
	if you in current_users :
		print(f"This {user} has already been used .")
	else :
		print(f"{user} is available !")


# ordinal numbers :

number_list=[1,2,3,4,5,6,7,8,9]

for number in number_list :
	if number == 1 :
		print(f"{number}st")
	elif number == 2 :
		print(f"{number}nd")
	elif number == 3 :
		print(f"{number}rd")
	else :
		print(f"{number}th")



# END ;




