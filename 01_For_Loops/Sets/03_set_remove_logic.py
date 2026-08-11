#Remove an Element from a Set
numbers = {10, 20, 30, 40, 50}
target = 30
new_set=set()
for i in numbers:
    if i!=target:
       new_set.add (i)
print(new_set)



#shorter
# numbers = {10, 20, 30, 40, 50}
# target = 30

# numbers.remove(target) 0r numbers.discar(target) 

# print(numbers)