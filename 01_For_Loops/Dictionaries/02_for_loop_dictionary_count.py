#dictionary that counts how many times each number occurs
numbers = [5, 10, 5, 20, 10, 5, 20]
repeat={}
for i in (numbers):
    count=0
    for n in numbers.copy():
        if i == n:
            count+=1
    repeat[i]=count
print(repeat)


#simple
# numbers = [10, 20, 10, 30, 20, 10]

# count = {}

# for number in numbers:
#     if number in count:
#         count[number]=count[number]+1
#     else:
#         count[number]=1
# print(count)