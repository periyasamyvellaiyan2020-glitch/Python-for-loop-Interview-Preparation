#Find the total marks for each student.
students = { "Arun": {"Math": 85,"Python": 90,"SQL": 80},
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
total_dict={}

for names,sub_mark in students.items():
    total=0
    for subject,score in sub_mark.items():
        total+=score
    total_dict[names]=total
print(total_dict)