#Problem 11 — Set Intersection Logic
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
common=set()
for i in a:
    found=False
    for n in b:
        if i==n:
            found=True
            break
    if found==True:
        common.add(n)
print(common)
