cars = ['bmw','audi','toyota','subaru']

cars.sort()
print(cars)
# sort() help to put the values in the alphabetical order 
cars.sort(reverse=True)
print(cars)
# sort(reverse=True)" the word 'true' need to be with an uppercase T " reverse the alphabetical order of the values
print("here is the original list :")
print(cars)
print("here is the sorted cars list :")
print(sorted(cars))
# sorted(name_of_the_list)help to put the values in the alphabetical order without deleting the first order of the list 
print(cars)
cars.reverse()
print(cars)
# reverse help to revert the list and you can go back by applying the same method for a 2nd time (to go to the first order)
print(f"The number of cars is : {len(cars)}")
#len() help to identify the number of items in a list 
"""
Summary :
the sort() method is permanently applied
the sorted() method is temporarily applied
the len() help finding the lengh of lists
the reverse() help reverse the lists
reversing a list a 2nd time return it to it original form 
"""
