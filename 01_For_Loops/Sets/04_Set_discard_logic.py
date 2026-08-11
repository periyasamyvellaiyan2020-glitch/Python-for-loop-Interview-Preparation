#discard an Element from a Set
numbers = {10, 20, 30, 40, 50}
target = 10
new_set=set()

for i in numbers:
    if i!=target:
       new_set.add (i)
       
print(new_set)
