#Problem 09 — Find the Average of Dictionary Values
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}

count,total=0,0

for score in marks.values():
    count+=1
    total=score+total
avg=total/count
print("Average marks:",avg)

