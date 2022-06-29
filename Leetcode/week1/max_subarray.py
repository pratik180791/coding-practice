ip = [5,4,-1,7,8]
#ip = [-2,1,-3,4,-1,2,1,-5,4]
#ip = [1]
#print(sum(ip))
max_sum = -1

for i in range(len(ip)):
    for j in range(i+1, len(ip)+1):
        #print(i, j)
        #print(ip[i:j])
        if sum(ip[i:j])>max_sum:
            max_sum = sum(ip[i:j])
    #print(ip[i:j])
print(max_sum)


max_subarr = ip[0]
local_subarr = ip[0]
for i in range(1, len(ip)):
    local_subarr = max(i, local_subarr+ip[i])
    max_subarr = max(max_subarr, local_subarr)
print(max_subarr)



