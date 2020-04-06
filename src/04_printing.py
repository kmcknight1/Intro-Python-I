import console
console.clear()
"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

y_rounded = ('%f' % round(y, 2))
y_rounded_without_zeros = y_rounded.rstrip('0')

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
format_01 = 'x is %i, y is %s, z is %s'
info = (x, y_rounded_without_zeros, z)
print(format_01 % info)

# Use the 'format' string method to print the same thing
format_02 = 'x is {}, y is {}, z is {}'
print(format_02.format(x, y_rounded_without_zeros, z))


# Finally, print the same thing using an f-string
format_03 = f"x is {x}, y is {y_rounded_without_zeros}, z is {z}"
print(format_03)
