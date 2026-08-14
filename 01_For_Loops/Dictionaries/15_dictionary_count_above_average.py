# *Problem 15 — Count How Many Values Are Above the Average
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
count=0
total=0
for score in marks.values():
    total=score+total
    count+=1
avg=total/count
print(avg)
above_avg=0
for score in marks.values():
    if score > avg:
        above_avg+=1
print(above_avg)
