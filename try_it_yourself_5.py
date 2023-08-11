# try it yourself using the slices :
pizzas = ['pepperoni','3chess','margerita','large','4seasons']
friend_pizzas = pizzas[:]
pizzas.append('big')
friend_pizzas.append('small')
# proof that they are two diffrente lists :
print("My favorite pizzas are :")
for pizza in pizzas:
	print(pizza.title())
 
print("\nMy friend's favorite pizzas are :")
for pizza in friend_pizzas  :
	print(pizza.title())
#End 


# The rest of try_it_yourself_5 is at the loop_3.py file /


















