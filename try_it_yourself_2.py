location_list = ['england','new_york','malisia','istanbul','sweden']
print("here is the original list :")
print(location_list)
print("here is the sorted list :")
print(sorted(location_list))
# sorting the location on the alphabetical order 
print("here is the original again list :")
print(location_list)
# The original list 
print("here is the sorted in an reverse alphabetical order list :")
print(sorted(location_list,reverse=True))
# to sorte the list in reverse alphabetical using the sorted() method I did add reverse=True after a ","
print("here is the original list :")
print(location_list)
location_list.reverse()
# I reversed the list using reverse() 
print("here is the reversed list :")
print(location_list)
print("here is the original list after reversing it the 2nd time :")
location_list.reverse()
# I used reverse again to return the list to it original form 
print(location_list)
print("here is the soted list permanently :")
location_list.sort()
#I did use the sort() the orginazed my list permanently 
print(location_list)
print("here is the sorted in an reverse alphabetical order list :")
location_list.sort(reverse=True)
print(location_list)
# using sort(reverse=True) help me order the list in a reverse alphabetical order permanently


print("\t*************************************************************")
print()
#there is part of this project in try_it_yourself_1 file !
print("the number of the location in the list : ")
print(len(location_list))












