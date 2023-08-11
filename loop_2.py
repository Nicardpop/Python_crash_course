#making numerical lists !
# using range() function :

for value in range(1,5):
	print(value)
#value is a variable / range function take two input or one
#range does not print the second number 
for value in range(6):
	print(value)

#in the case of one number the function print from 0 to the N-1('N'is the number given)
# range() inside of a list() to fill the list with numbers 
numbers=list(range(6))
print(numbers)
# I give range() a third number to skip numbers in that list :
even_numbers=list(range(2,10,2))
print(even_numbers)
# it kept adding 2 to the numbers and printing the result .
# in python ** represent exponents

squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)

print(squares,"\n")

# I started with a empty list and then I appending it with number between 1 and 10 to the power of 2 (value)
# I can easily find the max , min and the sum of a list by using max(),min(),sum()


#list comprehensions :

squares= [value**2 for value in range(1,11)]
print(squares)
