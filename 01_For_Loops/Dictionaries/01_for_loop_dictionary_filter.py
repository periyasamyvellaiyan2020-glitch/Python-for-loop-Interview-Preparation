#Create a new dictionary containing only subjects whose marks are below 70.
marks = {
    "Math": 85,
    "Science": 65,
    "English": 40,
    "Python": 90
}
filtered={}
for subject,mark in marks.items():
    if mark <70:
        filtered[subject]=mark
print(filtered)


#filtered.update({subject: mark}) = filtered[subject]=mark