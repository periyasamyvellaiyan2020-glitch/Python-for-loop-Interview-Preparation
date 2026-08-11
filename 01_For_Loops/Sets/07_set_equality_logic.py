#How can I prove that every element of a exists in b, AND every element of b exists in a?
a = set()
b = set()
count=0
if len(a)==len(b):
    for a_element in a:
        for b_element in b:
            if a_element==b_element:
                count+=1
                break
    if len(a)==count:
        print("Two Sets Are Equal")
    else:
        print("Two Sets Are NOT Equal")
else:
        print("Two Sets Are NOT Equal")
            
# a = {10, 20, 30}
# b = {30, 10, 200}

# # # The absolute fastest shortcut
# # if a == b:
# #     print("Two Sets Are Equal")
# # else:
# #     print("Two Sets Are NOT Equal")
