# #Problem 19 — Find the Subject with the Biggest Improvement

# We have old marks and new marks:
old_marks = {
    "Math": 70,
    "Science": 50,
    "English": 65,
    "Python": 40,
    "SQL": 55
}

new_marks = {
    "Math": 85,
    "Science": 60,
    "English": 72,
    "Python": 65,
    "SQL": 64
}

improved={}
big_improve={}
temp={}
for subject, score in old_marks.items():
    for new_subject,new_score in new_marks.items():
        if subject==new_subject:
            if score<new_score:
                improved[new_subject]=new_score
                break
print('improved_subjects',improved)

for subject, score in old_marks.items():
    for new_subject,new_score in new_marks.items():
        if subject==new_subject:
            diff=new_score-score
            temp[new_subject]=diff
greater=0
for i in temp.values():
    if i>greater:
        greater=i
for subject, difference in temp.items():
    if difference==greater:
        print(f"BIG IMPROVEMENT Subject: {subject} ,Improvement: {difference}")





