#Problem 10 — Set Union Logic
a = {10, 20, 30}
b = {30, 40, 50}
combined=set()
for i in a:
    combined.add(i)

for i in b:
    combined.add(i)
print(combined)