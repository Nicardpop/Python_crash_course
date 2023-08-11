bicycles =['trek','connondale','redlline','specialized']
#first item in a list is p0 not p1 
print(bicycles[0].title())
#.title() is for capitalizing the item 
print(bicycles[1].title())
print(bicycles[3].title())
message = f"My first bike was,{bicycles[0].title()}"
print(message)
 #using fstring to create a message using list 