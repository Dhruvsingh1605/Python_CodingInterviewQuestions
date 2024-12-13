def Counter(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict

a = Counter([1,2,3,1,2,4,5,6])
print(a)
