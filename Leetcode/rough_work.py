
a = [[1, 3], [5,1], [2, 2], [3,4], [6, 2]]

b = sorted(a, key=lambda x: x[0], reverse=True)
print(b)

c = sorted(a, key=lambda x: x[1])
print(c)

a= [1, 2, 4]
a.pop()