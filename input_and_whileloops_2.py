# introducing while loops :
"""DO NOT RUN THIS PROGRAM
# while loop in Action:

# counting.py :
current_number= 1
# while loop :
while current_number <= 5 :
	print(current_number)
	current_number += 1 

# letting the user choose when to quit :
# ex :

prompt="\nTell me something, and I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program. "

message =""
while message != 'quit':
	message=input(prompt)
	if message != 'quit' :# so that it dont print 'quit' and quit.
		print(message) 

# using flag :
prompt="\nTell me something, and I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program. "
# the flag :
active= True
# the loop : 
while active :
	message = input(prompt)
	if message == 'quit':
		active = False 
	else:
		print(message)

#using break to exit a loop :

# cities.py :
prompt ="\nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.)"

while True :
	message=input(prompt) 
	if message == 'quit':
		break# a while true loop run forever unless it reaches a break statement.
	else :
		print(f"\nI'd love to go to {message.title()}")

#we can use the break statement in any python loops .

#using a continue loop :

# continue return to the beginning of the loop :

current_number = 0 
while current_number < 10 :
	current_number += 1
	if current_number % 2 == 0 :
		continue 
	
	print(current_number)# to print the just odd numbers .
"""
# avoiding infinite loops : test every while loop and check that you set quit point.

# summary : flag-break-continue.
# Try it yourself :


# pizza toppings :

prompt = "Please enter your pizza toppings:"
prompt += "\n(Enter 'quit' when you finish) "

topping=""
while topping != 'quit' :
	topping=input(prompt)
	if topping != 'quit':
		print(f"\nI will add {topping} to your pizza. ")
print() 

# Movie tickets :

prompt="Please enter your age :"
prompt+= "\nEnter '0' to exit. "
active=True 
while active :
	age = input(prompt)
	age = int(age)
	if age == 0 :
		active=False 
	

	if age < 3:
		print("\nThe cost of the movie ticket is $0.")
	elif age < 12 :
		print("\nThe cost of the movie ticket is $10.")
	else  :
		print("\nThe cost of the movie ticket is $15.")

# infinity :
current_number=0
while current_number < 6 :
	print(current_number)

# end;











