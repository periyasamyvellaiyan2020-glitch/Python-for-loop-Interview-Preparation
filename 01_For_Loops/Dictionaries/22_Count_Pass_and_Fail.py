# Task
# Count how many subjects are:
# Pass → score >= 50
# Fail → score < 50
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}
pass_count = 0
fail_count = 0

for subject, score in marks.items():
    if score >=50:
        pass_count+=1
    else:
        fail_count+=1
print("Pass: ",pass_count)
print("Fail: ",fail_count)
    