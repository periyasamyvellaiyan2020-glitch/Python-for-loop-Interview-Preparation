#Write a normal Python program using the update() method.
a = {10, 20, 30}
k={30, 40, 50, 60}
for k_element in k.copy():
    found=False
    for a_element in a:
        if a_element==k_element:
            found=True
            break
    if found==False:
        a.add(k_element)
print(a)