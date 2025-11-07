fruits = ["apple", "bannana", "grapes", "orange"]
print(fruits)
print(fruits[0])

for fruit in fruits:
    print(fruit);

print(dir(fruits))


fruits.append("strawberry")

print(fruits)
print(len(fruits))

print("dog" in fruits)

fruits[2] = "pineapple"

for fruit in fruits:
    print(fruit)