#Find the subjects that both students have, and determine who scored higher in each common subject.
student_A = {
    "Math": 85,
    "Science": 70,
    "English": 72,
    "Python": 90
}

student_B = {
    "Math": 80,
    "Science": 75,
    "English": 72,
    "SQL": 88
}

for subject_A,score_A in student_A.items():
    for subject_B,score_B in student_B.items():
        if subject_A==subject_B:
            if score_A>score_B:
                print("student_A  IN",subject_A)
               
            elif score_B>score_A:
                print("student_B IN",subject_A)
                
            else:
                print("Both are equal in",subject_A)
    
