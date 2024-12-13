def sorting(num):
    ## [4, 1, 3, 6, 2, 7]
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] > num[j+1]:
                num = num[i] , num[j+1] = num[j+1] , num[i]
            elif num[i] < num[j+1]:
                continue
        return num
    
a = sorted([4, 2, 6, 1, 5])
print(a)