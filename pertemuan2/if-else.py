#pernyataan if
a = 23
b = 2007
if b > a:
 print("b lebih besar dari a")

#memeriksa apakah suatu angka positif
number = 25
if number > 0:
  print("angka tersebut adalah positif")

#beberapa pernyataan blok dalam if
age = 25
if age >= 26:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")#Multiple Statements in If Block

#menggunakan variabel dalam kondisi
is_logged_in = True
if is_logged_in:
  print("Selamat datang!")

#elif
a = 23
b = 23
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a and b sama")

#menguji berbagai kondisi dengan elif
score = 85

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

age = 70

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#pencarian hari dalam seminggu
day = 5

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#the else keyword
a = 2007
b = 23
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a and b sama")
else:
  print("a lebih besar dari b")

#the else withuout elif
a = 2007
b = 23
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#How Else Works
number = 9
if number % 2 == 0:
  print("angka tersebut genap")
else:
  print("angka tersebut ganjil")

#Complete If-Elif-Else Chain
temperature = 18
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Else as Fallback
username = "asa"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

 #Short Hand If
a = 75
b = 2
if a > b: print("a lebih besar dari b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#Assign a Value With If ... Else
a = 20
b = 30
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line
a = 223
b = 223
print("A") if a > b else print("=") if a == b else print("B")

#Practical Examples
x = 15
y = 25
max_value = x if x > y else y
print("Maximum value:", max_value)

#The and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("kedua kondisi benar")

#The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("setidaknya satu kondisi benar")

#The not Operator
a = 33
b = 200
if not a > b:
  print("a tidak lebih besar dari b")

#Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Nested If Statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#How Nested If Works
age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#The pass Statement
a = 33
b = 200

if b > a:
  pass

#pass in development
age = 18
if age < 18:
  pass  # TODO: Add underage logic later
else:
  print("Access granted")

#pass with Multiple Conditions
value = 55
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#Nested If Statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


