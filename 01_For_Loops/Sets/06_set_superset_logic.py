#Problem 06 — Superset Logic
a = {10, 20, 30, 40}
b = {10, 20, 30, 40,}
if len(a)>len(b):
    count=0
    for b_element in b:
        for a_element in a:
            if b_element==a_element:
                count+=1
                break
    if len(b)==count:
        print("a is the super set")
if len(a)==len(b):
    print('neither is a superset.')
else:
    count=0
    for a_element in a:
        for b_element in b:
            if b_element==a_element:
                count+=1
                break
    if len(a)==count:
        print("b is the super set")

    