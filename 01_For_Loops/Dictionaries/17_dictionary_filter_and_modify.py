#For every subject with a mark of 60 or more, add 5 bonus marks.
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
bonus={}
for subject,score in marks.items():
    if score>=60:
        score+=5
        bonus[subject]=score
print(bonus)


