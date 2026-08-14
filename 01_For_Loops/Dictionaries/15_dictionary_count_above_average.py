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


marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}

# avg = sum(marks.values()) / len(marks)

# above_avg = sum(score > avg for score in marks.values())

# print(f"Average: {avg}")
# print(f"Above average: {above_avg}")