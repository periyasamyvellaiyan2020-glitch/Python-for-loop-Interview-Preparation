# Given a non-empty list of integers, find the minimum value by manually traversing the list with a for loop
#without using the built-in min() function.
a=[4,5,89,2,97,95,854,9,894,56,4,14,4,]
minimum=a[0]
for i in a[1:]:
    if i<minimum:
        minimum=i

print(minimum)
print(min(a))