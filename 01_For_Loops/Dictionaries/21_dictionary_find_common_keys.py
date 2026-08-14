#Create a set containing the subjects that both students have.
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
# common=set()
# for subject_A in student_A.keys():
#     for subject_B in student_B.keys():
#         if subject_B==subject_A:
#             common.add(subject_A)
#             break


common=set(student_A) & set(student_B)
print(common)

common = student_A.keys() & student_B.keys()
print(common)