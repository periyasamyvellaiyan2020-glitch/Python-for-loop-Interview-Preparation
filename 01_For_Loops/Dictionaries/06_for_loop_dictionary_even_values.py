#Problem 07 — Find dictionary items whose value is even
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
filtered={}
for subject,score in marks.items():
    if score%2==0:
        filtered[subject]=score
print(filtered)
