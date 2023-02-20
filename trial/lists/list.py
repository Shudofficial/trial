# #python lists
names = ["samuel","musuu"]
numbers = [1,2,3,4,5,6,7,7,8,9]
decimals = [45, 9, 15.1,12.0,11.6]
print(decimals[0])
print(len(decimals)) #legtn of list
print(sum(numbers))
for i in range(len(numbers)):
    print(numbers[i])

#list methods
#index
print(numbers.index(4))

print(names.index("musuu"))
#append
for i in range(len(numbers)):
    print(numbers[i])

print("\n")
numbers.append(90)

#after appending
for i in range(len(numbers)):
    print(numbers[i])
print(numbers.count(7))

print(numbers.pop(2))

numbers.insert(2, 100)
for i in range(len(numbers)):
    print(numbers[i])

#after
numbers.sort()
#add a line for formatted output
print("\n")

for i in range(len(numbers)):
    print

fives=[5]*5

max(numbers)
min(numbers)
for i in range(10):
    numbers.append(i)
    #insert eleents
for i in range(len(numbers)):
    print(numbers[i])
