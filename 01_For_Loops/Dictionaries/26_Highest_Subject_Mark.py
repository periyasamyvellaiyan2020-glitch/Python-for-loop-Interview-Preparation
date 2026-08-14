# #26 — For each student, find:
# Their highest mark
# The subject in which they got that mark
students = {
    "Arun": {
        "Math": 85,
        "Python": 90,
        "SQL": 80
    },

    "Bala": {
        "Math": 75,
        "Python": 80,
        "SQL": 70
    },

    "Kumar": {
        "Math": 90,
        "Python": 85,
        "SQL": 95
    }
}
top={}
for names,sub_mark in students.items():
    highest=0
    highest_subject = ""
    for subject,score in sub_mark.items():
        if score > highest:
            highest=score
            highest_subject = subject
    top[names]=(highest_subject,highest)
print(top)
        

