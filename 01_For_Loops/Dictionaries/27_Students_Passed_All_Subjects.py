#A student passes all subjects only if every mark is >= 50.
# Find the students who passed every subject.
students = {
    "Arun": {
        "Math": 85,
        "Python": 90,
        "SQL": 80
    },

    "Bala": {
        "Math": 59,
        "Python":485,
        "SQL": 70
    },

    "Kumar": {
        "Math": 90,
        "Python": 85,
        "SQL": 95
    }
}
pass_list={}
for names,sub_mark in students.items():
    passed=False
    for subject,score in sub_mark.items():
        if score<50:
            passed=True
            break
    if passed==False:
        pass_list[names]=''
print(pass_list)
    
          