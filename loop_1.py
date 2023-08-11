# This is chapter 4 " working with lists. "
magicians = ['alice','david','carolina']
for magician in magicians: # the colon ":" is there to interpret the next line as the start of a loop !
	print(magician)# indent is for organization and without it an error is printed !
# python retrieve the name from the list and associatetes that value with the variable magician .
for magician in magicians :
	print(f"{magician.title()} ,that was a great trick")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
#indenting a line accidentally will show a error when executing !
