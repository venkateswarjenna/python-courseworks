grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_grades = dict(sorted(grades.items(), key=lambda item:
item[1]))
print(sorted_grades)
# Output: {'Charlie': 78, 'Alice': 85, 'Bob': 92}