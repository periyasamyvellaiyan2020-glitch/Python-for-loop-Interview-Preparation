#Problem 04 — Find the most repeated number
numbers = [5, 10, 5, 20, 10, 5, 20]
repeat={}
for i in numbers:
    if i not in repeat:
        repeat[i]=1
    else:
        repeat[i]=repeat[i]+1
print(repeat)

get_max=set()
for value in repeat.values():
    get_max.add(value)
    print(get_max)

