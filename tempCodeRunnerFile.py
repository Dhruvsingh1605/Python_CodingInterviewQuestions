def dict_sorting(dictionary):
    sorted_dict = {}
    a = list(dictionary.items())
    for i in range(len(a)):
        for j in range(len(a)+1):
            if a[j][1] > a[j+1][1]:
                a[j] , a[j+1] = a[j+1] , a[j]
            else:
                continue
    for key, value in a:
        sorted_dict[key] = value
    return sorted_dict

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a = dict_sorting(dictionary)
print(a)
    



