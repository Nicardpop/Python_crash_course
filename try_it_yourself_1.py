guest_list = []
guest_list.append('pablo')
guest_list.append('rodolfo')
guest_list.append('hasbulah')
guest_list.append('pepino')
print(guest_list)
print(f"{guest_list[0].title()}, I would like to have you for dinner .")
print(f"{guest_list[1].title()}, I would like to have you for dinner .")
print(f"{guest_list[3].title()}, I would like to have you for dinner .")
late_guest_list = []
print()
print("\t***********************************************")
late_guest_list.append('pablo')
late_guest_list.append('rodolfo')
late_guest_list.append('hasbulah')

print(late_guest_list)

guest_list.remove('pablo')
guest_list.remove('rodolfo')
guest_list.remove('hasbulah')

guest_list.append('nicard')
guest_list.append('dracin')
guest_list.append('george')
guest_list.append('dream')
print(guest_list)
print(f"{guest_list[0].title()}, I would like to have you for dinner .")
print(f"{guest_list[1].title()}, I would like to have you for dinner .")
print(f"{guest_list[2].title()}, I would like to have you for dinner .")
print(f"{guest_list[3].title()}, I would like to have you for dinner .")
print(f"{guest_list[4].title()}, I would like to have you for dinner .")
# here I removed late guest that can't make it and I added new ones 
print()
print("\t*********************************************")
guest_list.insert(0,'mouh')
guest_list.insert(4,'chakib')
guest_list.append('chocho')
print(f"The new guest list is : {guest_list}")
# here I put mouh in the 1P and chakib in the middle and chocho at the end 
print("\t*********************************************")
print("I can invite only two people to dinner ")
print(f"{guest_list[-1]} sorry but I can't invite you to dinner ")
popped_guest=guest_list.pop()
print(f"{guest_list[-1]} sorry but I can't invite you to dinner ")
popped_guest=guest_list.pop()
print(f"{guest_list[-1]} sorry but I can't invite you to dinner ")
popped_guest=guest_list.pop()
print(f"{guest_list[-1]} sorry but I can't invite you to dinner ")
popped_guest=guest_list.pop()
print(f"{guest_list[-1]} sorry but I can invite you to dinner ")
popped_guest=guest_list.pop()
print(f"{guest_list[-1]} sorry but I can invite you to dinner ")
popped_guest=guest_list.pop()
#using pop to minimize the guests number to 2 guests

print()
print("\t****************************************************")
print(guest_list)
print(f"{guest_list[0]} you are still invited to dinner ")
print(f"{guest_list[1]} you are still invited to dinner ")
#I use del here to empty the guests list 
print("\t****************************************************")
del guest_list[1]
del guest_list[0]
print("the guests list :")
print(guest_list)
# THE END



#from try_it_youself_2 
print("The number of guests in the list is : ")
print(len(guest_list))
