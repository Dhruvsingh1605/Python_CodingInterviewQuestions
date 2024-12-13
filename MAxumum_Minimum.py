""" The Question is we do not have to use the max() and min() methods
So the best way to do it is using .sort()
"""

def Max_Min(numbers):
    numbers.sort()
    return numbers[0], numbers[-1]

a = Max_Min([4, 5, 1, 6, 9])
print(f"Maximum and Mininum are - {a}")

# -----------------------------------------------------------------------------------------------------

def Without_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j-1]:
                numbers[i] , numbers[j-1] = numbers[j-1], numbers[i]
            else:
                continue
    return numbers

b = Without_sort([4, 5, 1, 6, 9])
print(f" Maximum and Minimum are - {b[0], b[-1]}")