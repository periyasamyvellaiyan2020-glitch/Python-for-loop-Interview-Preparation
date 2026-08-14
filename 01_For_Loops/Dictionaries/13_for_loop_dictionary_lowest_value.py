# 13 — Find the Lowest Value in a Dictionary
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
lowest=next(iter(marks.values()))
current_subject=0
print(lowest)
for subject, score in marks.items():
    if score<lowest:
        lowest=score
        current_subject=subject
print((f"lowest mark: {lowest} \n Subject: {current_subject}"))
