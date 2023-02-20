#nums=[9,10,2,5]
#x=nums[0]
#print(x

#replacing a value
nums=[10,20,50,6]
nums[2]=9
print (nums)

#appending a value
cars=["bmw","porshe","jeep"]
cars.append("toyota")
print (cars)

#removing
cars.remove("bmw")
print (cars)

#pop
numbers=[9,11,15,16]
numbers.pop(2)
print(numbers)

#len
numbers=[3,5,6,77,6,8]
length=len(numbers)
print(length)

#count
length=numbers.count(8)
print(length)

#reverse
numbers.reverse()
print(numbers)

numbers=[3,5,6,77,8,8,45,1]

for i in numbers:
    print(i)

numbers=[3,5,6,77,8,8,45,1]
for i in range(3):
    print(numbers[i])

name="climate"
#index
print(name[0])

# print(name[10])

#print the last
print(name[-1])

#print all letters in a string
for letter in name:
    print(letter)

#print 5 dashes
name1="sam"
name2="musuu"
print(name1+name2)

#to ask
name=input("enter name")
print("hello" +name)

#special charchters
name="samuel"
name3="musuu"
print(name)
print("/n")
print(name3)

#upper convert lower case 
name="ford"
print(name.upper())

print(name.lower())

#checking for alphabets
x="string345"
print(x.isalpha)

#for an app checking for an alphanumeric
password="srting345"
if password.isalpha():
    print ("invalid password")
else:
    print("valid password")

#ask for username
username=input("enter username")
print(username.upper)
print("hello "+ username.upper())

