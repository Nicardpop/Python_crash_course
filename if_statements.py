# CHAPTER 5:
# were learning about the if statement :
cars = ['audi','bmw','subaru','toyota']
# we want to print the bmw in uppercase and the rest title case :
for car in cars :
	if car == 'bmw': # we use the double equal sign to ask (true/false)
		print(car.upper())
	else:
		print(car.title())
# NOTE : We use the ":" after if and else .

requested_topping = 'mushrooms'

if requested_topping != 'anchovies' : # "!" ->  "not" 
	print('Hold the anchovies')
 # numerical comparisons :
age = 18
if age == 18 :
	print('\nTrue')
answer = 17
if answer != 42 :
	print('\nThat is not the correct answer. try again!')
# because 17 != 42 the intended code block is executed !
# comparisons using greater and less than ("<" and ">") , with = always in the right of em .

if age < 21 :
	print('True')
if age <= 21 :
	print('True')
if age > 21 :
	print('True')
else :
	print('False')
if age >= 21 :
	print('True')
else :
	print('False')
# checking multiple conditions :
# we use the key_work 'and' and 'or' :
if age >= 21 and answer >= 21 : # the two condition should be true together or the if wont print true .
	print('True')
else :
	print('False')
if age >= 18 or answer >= 18 :# its only need one condition to be true to pass .
	print('True')
else :
	print('False')
print('*************************************************')

# checking whether a value is in a list :
# we use the key_word "In" or "not in":
banned_users =['andrew','carolina','david']
user = 'marie'
if user in banned_users :
	print(f"{user.title()}, you can't post a response !")
if user not in banned_users :
	print(f"{user.title()} , you can post a response if you wish")


print('********************************************************************')

# Try_it_yourself :
	#conditional tests :
fruit = ['banana','apple','beets','avocado','pineapple']
print("is the fruit == 'banana' , I predict True")
# sometimes when we're dealing with boolean values we dont use if but we use this instead :
print(fruit == 'banana')
print("\nIs the fruit == 'orange' , I predict False")
print(fruit == 'orange')
print("\nIs the fruit == 'apple' , I predict True")
print(fruit == 'apple')
print("\nIs the fruit == 'onion' , I predict False")
print(fruit == 'onion')
print("\nIs the fruit == 'beets' , I predict True")
print(fruit == 'beets')
print("\nIs the fruit == 'mushrooms' , I predict False")
print(fruit == 'mushrooms')
print("\nIs the fruit == 'avocado', I predict True")
print(fruit=='avocado')
print("\nIs the fruit == 'pineapple',I predict True")
print(fruit=='pineapple')
print("\nIs the fruit =='mango', I predict False")
print(fruit=='mango')
print("\nIs the fruit == 'cantalope', I predict False")
print(fruit=='cantalope')
print("\n**********************************************")
# more conditional tests :

string_0 ="I love python"
string_1 ="I use python"
print(string_1 == string_0)
print(string_1!= string_0)
print()
string_2 = "I can't wait to finish this book"
string_3 ="i can't wait to finish this book"
print(string_2.lower()==string_3)
print(string_2==string_3)
print()
list_users = ['chocho','pablo','pepino','nicard']
if 'pepino' in list_users :
	print("Hello pepino !")

if 'mouh' not in list_users :
	print("please join")
  # end;
# End ;
