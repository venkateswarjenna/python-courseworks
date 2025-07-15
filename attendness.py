# List of students
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Dictionary to store attendance
attendance = {}

# Taking attendance using loop
for student in students:
    status = input(f"Mark attendance for {student} (P/A): ").strip().upper()
    
    if status == "P":
        attendance[student] = "Present"
    elif status == "A":
        attendance[student] = "Absent"
    else:
        print("Invalid input! Marked as Absent by default.")
        attendance[student] = "Absent"

# Display attendance summary
print("\n📋 Attendance Summary:")
for student, status in attendance.items():
    print(f"{student}: {status}")
