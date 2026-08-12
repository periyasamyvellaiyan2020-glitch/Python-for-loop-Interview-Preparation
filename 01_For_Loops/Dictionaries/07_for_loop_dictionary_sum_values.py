#Problem 08 — Find the Sum of All Dictionary Values
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
total_marks=0
for score in marks.values():
    total_marks+=score
print("Total marks:",total_marks)