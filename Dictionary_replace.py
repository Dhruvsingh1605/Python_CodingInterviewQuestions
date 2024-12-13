def Dictionary(dictionary, value, new_value):
    for i in dictionary:
        if dictionary[i] == value:
            dictionary[i] = new_value
    return dictionary

a = Dictionary({1: 'apple', 2:'guava',3:'grapes'},'apple','banana')
print(a)