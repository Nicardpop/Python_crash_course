# Chapter 9 :

# creating the dog class :

class dog :
  
  def __init__(self,name,age) :
    self.name = name
    self.age = age 
    
  def sit(self):
    print(f"{self.name} is now sitting.")
    
  def roll_over(self):
    print(f"{self.name} rolled over!")
    
#making an instance from a class :

# my_dog = dog('joji', 5)

# print(f"My dog's name is {my_dog.name}")
# print(f"\nMy dog's age is {my_dog.age} years old.\n")

# my_dog.sit()
# my_dog.roll_over()


#try is yourself :

#Restaurant :

# class Restaurant :
  
#   def __init__(self,res_name,cuisine_type):
#     self.name = res_name
#     self.type = cuisine_type
  
#   def describe_restaurant(self):
#     print(f"The name of the Restaurant is :{self.name}")
#     print(f"The type of the cuisine is {self.type}")
    
#   def open_restaurant(self):
#     print(f"The Restaurant {self.name} is open!")
    
    
# pablo = Restaurant('pablo','algerian')

# pablo.describe_restaurant()

# pablo.open_restaurant()