#build your own for + if logic to determine whether every element of a exists in b.
a = {10, 20}
b = {10, 20, 30, 40}
size=len(a)
count=0
for a_element in a:
    for b_element in b:
        if a_element==b_element:
            count+=1
            break
if size==count:
    print('a is subset of b')
else:
    print("a is not subset of b")
