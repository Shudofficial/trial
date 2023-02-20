import operators
x = operators.add(12, 34)


y = operators.subtract(45, 89)
print(y)

from operators import add
f = add(23, 43)

from operators import subtract
g = subtract (89, 34)
import others
others.cube(5)

#get 2 numbers
num1 = eval(input("enter number 1: "))
num2 = eval(input("enter operator 2: "))
Operator = input("enter operator: ")

if Operator == "+":
    x = operators.add(num1, num2)
    print(x)

if Operator == "-":
    x = operators.subtract(num1, num2)
    print(x)

if Operator == "/":
    x = operators.divide(num1, num2)
    print(x)

elif Operator == "*":
    x = operators.multiply(num1, num2)

elif Operator == "3":
    x = others.cube(num1)

print(x)
import math

# Get user input
num = float(input("Enter a number: "))

# Get user choice
choice = input("Enter 'sin' to get the sine, 'cos' to get the cosine, or 'tan' to get the tangent: ")

# Calculate trigonometric function based on user choice
if choice == 'sin':
    result = math.sin(num)
    print("The sine of", num, "is", result)
elif choice == 'cos':
    result = math.cos(num)
    print("The cosine of", num, "is", result)
elif choice == 'tan':
    result = math.tan(num)
    print("The tangent of", num, "is", result)
else:
    print("Invalid choice. Please enter 'sin', 'cos', or 'tan'.")

