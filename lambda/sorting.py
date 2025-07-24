students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sort by marks (2nd element of tuple)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]