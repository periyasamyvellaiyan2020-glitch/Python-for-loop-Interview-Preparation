#For each subject, find the highest mark among the three students and store the result in a new dictionary
student_A = {
    "Math": 85,
    "Science": 70,
    "English": 72,
    "Python": 90
}

student_B = {
    "Math": 80,
    "Science": 75,
    "English": 65,
    "Python": 70
}

student_C = {
    "Math": 90,
    "Science": 60,
    "English": 80,
    "Python": 85
}
max_scores={}
for subject,score_A in student_A.items():
    score_B=student_B[subject]
    score_C=student_C[subject]
    if score_A>score_B and score_A > score_C:
        max_scores[subject]=score_A
    elif score_B > score_C:
        max_scores[subject]=score_B
    else:
        max_scores[subject]=score_C
print(max_scores)


