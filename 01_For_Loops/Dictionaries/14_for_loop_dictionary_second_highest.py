#Problem 14 — Find the Second Highest Mark
marks = {
    "Math": 85,
    "Science": 46,
    "English": 72,
    "Python": 31,
    "SQL": 64
}

highest = 0
second_highest = 0

for subject, score in marks.items():

    if score > highest:
        second_highest = highest
        highest = score

    elif score > second_highest:
        second_highest = score

print(f"Highest: {highest}")
print(f"Second Highest: {second_highest}")

# shorter
# second_highest = sorted(marks.values(), reverse=True)[1]

# print(second_highest)
