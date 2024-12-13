def Max_repeating(number):
    dictionary = {}
    for i in number:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

a = Max_repeating([1, 2, 1, 2, 2, 3])
maximum = max(a.values())
for key, value in a.items():
    if value == maximum:
        print(f" most repeated value = {key}")
    