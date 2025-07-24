def multiply_by(n):
    return lambda x: x * n
double = multiply_by(2)
triple = multiply_by(3)
print(double(5)) # Output: 10
print(triple(5)) # Output: 15