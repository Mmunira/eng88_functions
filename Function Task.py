# Build a basic object Orientated Calculator
# phase 1: build a simple calculator class containing add, subtract, multiply, divide.
# phase 2: expand by creating:
# Divisible by method that returns true or false dependent on the outcome
# Work out and return the area of a triangle
# inch to cm converter
# NOTE -> Must be in class and method format


# class calculator:
#     def add(a, b):
#         return a + b
#     print(add(5, 2))
#     def subtract(a, b):
#         return a - b
#     print(subtract(5, 2))
#     def multiply(a, b):
#         return a * b
#     print(multiply(5, 2))
#     def divide(a, b):
#         return a / b
#     print(divide(5, 2))
#
# def divisible(a,b):
#     return True if a % b == 0 else False
# print(divisible(5,2))


# Work out and return the area of a triangle
# inch to cm converter

# semi_perimter: (a + b + c)/2
# area of triangle = (s*(s-a)*(s-b)*(s-c))-1/2


def trianglearea(a, b, c):
    sp = (a + b + c)/2
    return (sp * (sp - a) * (sp - b) * (sp - c)) ** 0.5
a = float(input("Enter first side of the triangle:"))
b = float(input("Enter second side of the triangle:"))
c = float(input("Enter third side of the triangle:"))

print('Area of triangle is: {0:.2f}'. format(trianglearea(a, b, c)))









