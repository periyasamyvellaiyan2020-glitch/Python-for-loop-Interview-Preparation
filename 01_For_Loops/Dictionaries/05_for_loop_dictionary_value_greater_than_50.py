#Problem 06 — Find keys whose value is greater than 50
marks = {
    "Math": 85,
    "Science": 45,
    "English": 72,
    "Python": 30,
    "SQL": 65
}
filtered={}
for subject,score in marks.items():
    if score>50:
        filtered[subject]=score
print(filtered,end='\n')

