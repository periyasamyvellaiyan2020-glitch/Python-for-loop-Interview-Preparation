#Problem 10 — Find the Highest Mark AND Student's Name
marks = {
    "Math": 85,
    "Science": 46,
    "English": 725,
    "Python": 91,
    "SQL": 64
}
highest=0
current_subject=0
for subject,score in marks.items():
    if score > highest:
        highest=score
        current_subject=subject
print(f"Highest mark: {highest} \n Subject: {current_subject}")


    