def Exception_hai(num):
    sum = 0
    for i in range(len(num)):
        if num[i] == 1:
            raise Exception(f" {1} found in the list")
        else:
            sum += i
    return sum

try:
    result = Exception_hai([2, 1, 4, 4])
    print("Sum:", result)
except Exception as e:
    print(e)