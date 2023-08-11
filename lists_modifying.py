motocycles =['honda','yamaha','suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)
# append() help to add a item at the end of the list
bicycles =[]
bicycles.append('trek')
bicycles.append('connondale')
bicycles.append('redline')
bicycles.append('specialized')
print(bicycles)

motocycles.insert(0,'MTB')
print(motocycles)
# insert() help to add an item in a N position

del motocycles[0]
print(motocycles)
# using del help deleting an item of a N position
popped_motocycles = motocycles.pop()
print(motocycles)
print(popped_motocycles)
# pop() is to remove the last item from the end and store it in a list
print(f"The last motorcycle I owned is {popped_motocycles.title()}")
first_owned = bicycles.pop(0)
print(f"The first bicycles I owned is {first_owned.title()}")
# pop(N) remove the N item from the list and store it in a variable 
motocycles.remove('honda')
print(motocycles)
# remove() help to delete the item by it value 
too_expensive = 'yamaha'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive for me. ")
# we assign the value 'yamaha' to a variable called too_expensive , allowing us to use it after the removal
# summery : insert(),append(),del,remove(),pop() and pop(N) , all of this previous methods help to remove,add or delete permently or with the kept of the deleted value


