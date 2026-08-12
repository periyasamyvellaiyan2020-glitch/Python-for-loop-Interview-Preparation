#11_for_loop_dictionary_Convert Negative Values to Positive

numbers = {
    "A": -10,
    "B": 20,
    "C": -30,
    "D": 40,
    "E": -50
}
modified={}
for letter,number in numbers.items():
    
    modified[letter]=abs(number)
print(modified)