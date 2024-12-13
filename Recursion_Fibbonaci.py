def fibbonaci_recursion(num):
    if num <= 1:
        return num
    else:
        return fibbonaci_recursion(num-1) + fibbonaci_recursion(num-2)

a = fibbonaci_recursion(10)
for i in range(10):
    print(fibbonaci_recursion(i))