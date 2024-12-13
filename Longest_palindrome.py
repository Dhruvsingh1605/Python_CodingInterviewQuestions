# def longest_palindrome(a):
#     for i in a:
#         if a[i::] == a[::-i]:
#             # return


            
a = "abba"
for i in a:
    print(a[i::], a[::-i])