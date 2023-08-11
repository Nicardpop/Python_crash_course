
# slicing a list :
# to slice a list you need to :
players=['charles','martina','michael','florence','eli']
print(players[0:3])#to slice I use ":"
print(players[1:4])# I can start wherever i want and finish too
print(players[:4])# I need to use the ':' or python will make a logic error(that the code work but output the wrong answer) !
print(players[2:])#I use the ':' after the first argument so python print starting from the argument till the end .
print(players[-3:])# same ^ , its output the last three players .
print(players[0:3:2])# same concept of the range() function : I added a third value to skip an element in the list .
# Looping through a slice :
print("here are the first three players in my team :")
for player in players[:3]:
	print(player.title())
	# to loop only through the slice  .

# copying a list :
# To copy a list all I had to do is to make a variable and store this inside it :
my_foods=['pizza','falafel','carrot cake']
friend_foods = my_foods[:]# I used my_foods[:] so I don't right all the list again . and thats how I copied the entier list 

print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are :")
print(friend_foods)

# We add new food to each one to show that's each list keeps track of the appropriate person's favorite foods :
my_foods.append('cannoli')
friend_foods.append('ice cream')
# we print the new list :
print("\nMy favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are :")
print(friend_foods)
 # summary : to copy a list use the slice method .
print("********************************************")
print()
print()
my_foods.append('chicken')
 # try_it_yourself 4-10 :
 #slices:
print("the first three items in the list are :")
print(my_foods[0:3])
print("\nThree from the middle of the list are :")
print(my_foods[1:4])
print("\nThe last three items in the list are :")
print(my_foods[-3:])
print()
print("\nMy favorite foods are :")
for food in my_foods :
	print(food.title())

print("\nMy friend's favorite foods are :")
for food in friend_foods:
	print(food.title())
 #end
#End
