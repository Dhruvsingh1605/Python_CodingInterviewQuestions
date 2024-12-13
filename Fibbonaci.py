def fibonnaci(num):
    lst =[0,1]
    for i in range(num):
        a = lst[i] + lst[i+1]
        lst.append(a)
    return lst

b = fibonnaci(10)
print(b)

## Slowely and Gradually You are getting there...