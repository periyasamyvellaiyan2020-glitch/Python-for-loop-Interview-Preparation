
numbers = {10, 20, 3,4,654,69,465,6,46,45,64,6,5, 40, 50}

selected = None
new_set = set()

for i in numbers:
    if selected is None:
        selected = i
    else:
        new_set.add(i)

print("Removed:", selected)
print("Remaining:", new_set)

# Python follows the set's internal iteration order.

# That order is not something you should rely on, because sets are unordered.