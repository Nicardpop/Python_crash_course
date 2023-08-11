# try it yourself :

#Deli :

sandwich_orders=['tuna','beef','pastrami','chicken']
finished_sandwichs=[]

while sandwich_orders :
	sandwich=sandwich_orders.pop()
	print(f"I made your {sandwich.title()} sandwich. ")
	finished_sandwichs.append(sandwich)
print("\nList of ordered sandwichs :")
for sandwichs in finished_sandwichs :
	print('\t'+sandwichs.title()+"sandwich")

# No pastrami :

sandwich_orders=['pastrami','tuna','beef','pastrami','chicken','pastrami',]

print("The deli has run out of Pastrami! ")

while 'pastrami' in sandwich_orders :
	sandwich_orders.remove('pastrami')
print("\nAvailible Sandwichs :")
for sandwich in sandwich_orders :
	print(sandwich.title()+" sandwich. ")

# dream vacation :

prompt="If you could visit one place in the world,"
prompt+="\nWhere would you go? "

places=[]
while True :
	responce=input(prompt)
	places.append(responce)
	repeat=input("Another one?(yes/no) ")
	if repeat == 'no' :
		break
		
print("--- polling result ---")
for place in places :
	print(responce.title())	

# End;
# End of chapter 7;

















