
a = "cbbd"
a = "a"
a = "ac"
a = "bb"
a = "babad"
a = "abb"

def longest_palind(ip: str)-> str:
    op = ""
    if not ip:
        return op
    if ip == ip[::-1]:
        return ip
    op = ip[0]
    for i in range(len(ip)):
        for j in range(i+1, len(ip)+1):
            temp = ip[i:j]
            if len(temp) > len(op) and temp == temp[::-1]:
                op = temp
    return op

op = longest_palind(a)
print(op)


from collections import Counter

