#Build your own logic to find:#Elements that exist in a but NOT in b.
# 
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
temp_set=set()
diff_set=set()

for a_element in a:
    for b_element in b:
        if a_element==b_element:
            temp_set.add(a_element)
            break

for a_element in a:
    same=False
    for temp in temp_set:    
        if a_element == temp:
            same=True
            break
    if same==False:
         diff_set.add(a_element)
print(diff_set)
        




