#Problem 04 — Find the most repeated number
numbers = [5, 10, 5, 20, 10, 5, 20]
repeat={}
for i in numbers:
    if i not in repeat:
        repeat[i]=1
    else:
        repeat[i]=repeat[i]+1
print(repeat)

get_max=[]
for value in repeat.values():
    get_max.append(value)
print(get_max)

higher=get_max[0]
for i in get_max:
    if i>higher:
        higher=i
print(higher)

for number, count in repeat.items():
    if count == higher:
        print(f"The most repeated number is:{number}")

# repeat = {5: 3, 10: 2, 20: 2}

# number = max(repeat, key=repeat.get)

# print(number)