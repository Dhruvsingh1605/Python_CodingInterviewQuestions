def string_operations(senetence):
    s = ''
    if not isinstance (senetence, str):
        senetence = str(senetence)
    for i in senetence:
        if ((i >= 'A' and i<='Z') | (i>= 'a' and i <='z') | (i == ' ')):
            s = s+i
    return s
def reverse_string(s):
    s = s[::-1]
    return s

sentence = "Hey # there $ motherfucker!"
a = string_operations(sentence)
b = reverse_string(sentence)
print(a)
print(b)