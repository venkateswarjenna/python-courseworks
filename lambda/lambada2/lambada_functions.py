

#1 Check if a number is positive, negative, or zero
check_number = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(check_number(5))  
print(check_number(0))    
print(check_number(-3))


#2. Extract first letter from each word
words = ["Python", "Lambda", "Function"]
first_letters = list(map(lambda w: w[0], words))
print(first_letters)  

#3. Filter names longer than 4 characters
names = ["Venky", "Manoj", "Lakshman", "Ravi"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names) 

#4. Convert temperature from Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  

#5 Find words containing a specific letter ('e')
words = ["apple", "banana", "cherry", "fig"]
with_e = list(filter(lambda word: 'e' in word, words))
print(with_e)  


#6  Lambda to reverse a string
reverse = lambda s: s[::-1]
print(reverse("python"))  

#7 Calculate square and cube using map and lambda
nums = [1, 2, 3]
squares_cubes = list(map(lambda x: (x, x**2, x**3), nums))
print(squares_cubes)  
#8 Sort a list of numbers in descending order using lambda
nums = [5, 3, 9, 1]
sorted_desc = sorted(nums, key=lambda x: -x)
print(sorted_desc)  

#9 Use lambda in list comprehension
double_if_even = [(lambda x: x*2 if x % 2 == 0 else x)(i) for i in range(1, 6)]
print(double_if_even)  

#10 Sum of digits using reduce + lambda
from functools import reduce

number = 12345
digit_sum = reduce(lambda x, y: int(x) + int(y), str(number))
print(digit_sum)  