#Problem 16 — Create a Dictionary of Above-Average Marks
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
above_avg={}
avg=sum(marks.values())/len(marks)
for subject,score in marks.items():
    if score>avg:
        above_avg[subject]=score
print(above_avg)