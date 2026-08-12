#Problem 03 — Count Without Repeating Work
numbers = [5, 10, 5, 20, 10, 5, 20]

repeat = {}

for i in numbers:
    if i not in repeat:
        repeat[i]=1
    else:
        repeat[i]=repeat[i]+1
print(repeat)
