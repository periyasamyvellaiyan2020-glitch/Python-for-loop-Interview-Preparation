#Problem 10 — Double Every Dictionary Value
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 91,
    "SQL": 64
}

multiple={}
for subject,score in marks.items():
    score=score*score
    multiple[subject]=score
print(multiple)