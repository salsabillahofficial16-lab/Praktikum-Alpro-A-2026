#Creating a Function
print("Hello from a function")

#Calling a Function
def my_function():
  print("Hello from a function")
my_function()

#Without functions - repetitive code
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

#Return Values
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#The pass Statement
def my_function():
  pass

#A function with one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("lionel")
my_function("karl")
my_function("tobi")

#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("lionel", "Refsnes")

#Default Parameter Values
def my_function(country = "Norway"):
  print("I am from", country)

my_function("korea")
my_function("italy")
my_function()
my_function("japan")

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "buddy", age = 7)

#Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["strawberry", "grape", "orange"]
my_function(my_fruits)

#Return Values
def my_function(x, y):
  return x + y

result = my_function(4, 5)
print(result)

#Returning Different Data Types
def my_function():
  return ["strawberry", "grape", "orange"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("lionel")

#Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "lionel")

#Combining Positional-Only and Keyword-Onl
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#Mengakses argumen individual dari *args
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "lionel", "mail", "Linus")

#Practical Example with *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(4))

#Accessing values from **kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#Using **kwargs with Regular Arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

#Combining *args and **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#A variable created inside a function is available inside that function
def myfunc():
  x = 3007
  print(x)

myfunc()

#The local variable can be accessed from a function within the function
def myfunc():
  x = 3007
  def myinnerfunc():
    print(x)
  myinnerfunc()

#myfunc()
# my_function()

# def get_greeting():
#   return "Hello from a function"

# message = get_greeting()
# print(message)

# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)

# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)