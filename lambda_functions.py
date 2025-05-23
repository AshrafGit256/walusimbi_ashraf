#lambda functions

# Definition
# It is used for small functions, and we use a lambda key word


# def add(a, b): return a + b

# print(add(10, 5))

# square = lambda  x: x*x
# print(square(2))

# add = lambda a, b : a + b
# print(add(10, 5))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))
print(squared)

# Assignment one : Find the factorial of a number (five)