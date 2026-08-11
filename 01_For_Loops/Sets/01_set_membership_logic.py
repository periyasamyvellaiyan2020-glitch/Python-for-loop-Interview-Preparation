#write your own for-loop logic to determine whether target exists in the set.
numbers = {10, 20, 30, 40, 50}
target = 10
target_found=False
for i in numbers:
    if target==i:
        print(f"{target} exists")
        target_found=True
        break
if target_found==False:
    print(f"{target} does not exist")




#     #shorter
#     numbers = {10, 20, 30, 40, 50}
# target = 10

# print(target in numbers)