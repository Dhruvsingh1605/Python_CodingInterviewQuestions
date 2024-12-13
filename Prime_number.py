def prime_number(upper, lower):
    for num in range(upper, lower):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num,end=", ")
a = prime_number(1,100)
print(a)