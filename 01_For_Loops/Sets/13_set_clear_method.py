# Start with the set.
# Remove all elements using your own logic.
# Print the final set.

# numbers = {10, 20, 30, 40, 50}

# new_set = set()

# numbers = new_set

# print("Remaining:", numbers)
    

numbers = {10, 20, 30, 40, 50}

new_set = set()

for i in numbers:
    if i not in numbers:
        new_set.add(i)

numbers = new_set

print("Remaining:", numbers)
