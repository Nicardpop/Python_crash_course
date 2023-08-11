#DO NOT EXECUTE IT > ! <

print("Counting to 20 : \n")
for value in range(1,21) :
	print(value)
print("********************************************")

#printing 1000000 using for function
numbers=list(range(1000001))
for number in numbers:
	print(number)
#finding odd numbers using 3rd argument of the range() function
for value in range(1,21,2):
	print(value)
print("********************************************")
# printing multiples of 3 :
for value in range(3,31,3):
	print(value)
print("********************************************")
# printing the numbers between 1 to 10 to the power of 3 :
for value in range(1,11):
	print(value**3)
print("********************************************")
#cube but this time using comprehensions :
numbers = [value**3 for value in range(1,11)]
print(numbers)

#End;
