def fibbonaci(num):
    a, b = 0, 1
    while True:
        yield a
        a , b = b, a+b

f1 = fibbonaci(num = int(input()))
# num = int(input())
for i in range(num = int(input())):
    print(fibbonaci(f1))
