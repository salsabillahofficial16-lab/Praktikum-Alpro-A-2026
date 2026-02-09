print(50 + 40)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum3)

#operator aritmatika
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#pembagian dalam python
x = 27
y = 7

print(x / y)
x = 27
y = 7

print(x // y)

#operator walrus
numbers = [5,6,7,8,9,10 ]
if (count := len(numbers)) > 7:
    print(f"List has {count} elements")

#operator perbandingan
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x is y)

#logika operator
x = 5
print(x > 0 and x < 10)
x = 5
print(x < 5 or x > 10)
x = 5
print(not(x > 3 and x < 10))

#identity operator
x = ["Mangga", "Blueberry"]
y = ["Mangga", "Blueberry"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["Blueberry", "Mangga"]
y = ["Blueberry", "Mangga"]
print(x is not y)

#difference betwween == and is
x = [5, 6, 7]
y = [5, 6, 7]

print(x == y)
print(x is y)

#membership operator
fruits = ["apple", "banana", "cherry"]
print("cherry" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#membership operator dengan string
text = "Hai indonesia"
print("H" in text)
print("Hai" in text)
print("s" not in text)

#bitwise operator
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#operator precedence
print(5 + 4 - 7 + 3)
print((9 + 3) - (9 + 3))
print(200 + 2 * 3)
print(5 + 4 - 7 + 3)

