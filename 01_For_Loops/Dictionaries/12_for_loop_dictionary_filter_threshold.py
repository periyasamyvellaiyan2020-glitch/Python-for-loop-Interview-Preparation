#Problem 14 — Filter Values Below a Threshold only the subjects whose marks are 60 or more.
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
filtered={}
for subject,score in marks.items():
    if score >=60:
        filtered[subject]=score
print(filtered)
