def palindrome(a):
    if a != str:
        a = str(a)
    if a[::] == a[::-1]:
        print(a[::], a[::-1])
        return True
    else:
        return False
    
b = palindrome(1221)
print(b)

