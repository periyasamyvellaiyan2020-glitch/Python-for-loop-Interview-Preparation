# 🎯 Task
# Calculate the total marks of each student.
# Compare the three totals.
# Find the student who has the highest overall total.
# Print the student's name and total marks
student_A = {
    "Math": 85,
    "Science": 70,
    "English": 72,
    "Python": 90
}

student_B = {
    "Math": 80,
    "Science": 75,
    "English": 65,
    "Python": 70
}

student_C = {
    "Math": 90,
    "Science": 60,
    "English": 80,
    "Python": 85
}
total_A=0
for score in student_A.values():
    total_A+=score
total_B=0
for score in student_B.values():
    total_B+=score  
total_C=0
for score in student_C.values():
    total_C+=score

print('student_A',total_A)
print('student_B',total_B)
print('student_C',total_C)
if total_A>total_B and total_A >total_C:
    print('student_A',total_A)
elif total_B>total_C:
    print('student_B',total_B)
else:
    print('student_C',total_C)