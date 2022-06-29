ip = ["eat","tea","tan","ate","nat","bat"]
#ip = ["a"]
mapper = {}
for i in ip:
    curr_val = "".join(sorted(i))
    #print(curr_val)
    if curr_val in mapper:
        map_val = mapper.get(curr_val)
        map_val.append(i)
        mapper.update({curr_val: map_val})
    else:
        mapper[curr_val] = [i]

res = [i for i in mapper.values()]

print(mapper)


print(res)