# Using to id() function to return the memory address
# The id() of a has been printed on line 10
# Try to add the print of id() for b and c
# Try to run more than 1 times and observe the changing values

print(id(5))
a = 5
b = a
c = 5.0
print(id(a))
print(id(b))
print(id(c))