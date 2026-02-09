#Python For Loops
fruits = ["strawberry", "grape", "orange"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "apple":
  print(x)

#The break Statement
fruits = ["strawberry", "grape", "orange"]
for x in fruits:
  print(x)
  if x == "grape":
    break

#The continue Statement
fruits = ["strawberry", "grape", "orange"]
for x in fruits:
  if x == "orange":
    continue
  print(x)

#The range() Function
for x in range(4):
  print(x)

for x in range(2, 4):
  print(x)

#Else in For Loop
for x in range(4):
  print(x)
else:
  print("Finally finished!")

for x in range(4):
 if x == 3: break
 print(x)
else:
  print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["strawberry", "grape", "orange"]
for x in adj:
  for y in fruits:
   print(x, y)

#The pass Statement
for x in [0, 1, 2]:
  pass