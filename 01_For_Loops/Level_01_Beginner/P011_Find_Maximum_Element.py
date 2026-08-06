#Given a non-empty list of integers, find the maximum value by manually iterating through the sequence using a for loop.

#Do not use the built-in max() function.
arr=[1,2,3,4,5,699,55,77,33]
maximum=arr[0]
for i in arr:
    if i>maximum:
        maximum=i
print(maximum)