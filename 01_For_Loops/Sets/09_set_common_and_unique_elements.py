# 1. Common elements
# 2. Elements only in A
# 3. Elements only in B

a = {10, 20, 30, 40}
b = {10, 30, 50, 60}
common_elements = set()
a_only=set()
b_only=set()
for a_element in a:
    for b_element in b:
        if a_element==b_element:
            common_elements.add(a_element)
print('common',common_elements)

for a_element in a:
    found=False
    for common in common_elements:
        if a_element == common:
            found=True
            break
    if found==False:
        a_only.add(a_element)
print('Elements only in A',a_only)

for b_element in b:
    found=False
    for common in common_elements:
        if b_element == common:
            found=True
            break
    if found==False:
        b_only.add(b_element)

print('Elements only in B',b_only)


