def sum_equal(lst, num):
    for i in range(len(lst)):
        for j in range(len(lst)):
            a = lst[i] + lst[j-1]
            if a == num:
                print(f"num_1 = {lst[i]} + num_2 = {lst[j]} = {a}")
                break
            else:
                continue
            
lst = [2,3,4,5,6]
a = sum_equal(lst, 10)
print(a)