
nums = [1,2,3,4]
op = [24,12,8,6]
nums = [-1,1,0,-3,3]
nums = [1,2,3,4]
#nums = [0, 0]
nums = [0, 4, 0]

from typing import List

def productOfArray(nums: List) -> List:
    total_product = 1
    zero_val = False
    cnt = 0
    for i in nums:
        if i == 0:
            zero_val = True
            cnt+=1
            continue
        total_product = total_product*i
    product_list = []

    for i in nums:
        if zero_val:
            if i == 0:
                if cnt>1:
                    return [0]*len(nums)
                else:
                    product_list.append(total_product)
            else:
                product_list.append(0)
        else:
            product_list.append(total_product//i)
    print(product_list)
    return product_list

op = productOfArray(nums)
#print(op)

def productOfArrayWithoutDiv(nums: List)-> List:
    result_list = [0]*len(nums)
    result_list[0] = 1
    #right[-1] = 1
    total_mul = 1
    for i in range(0, len(nums)):
        result_list[i] = total_mul
        total_mul*=nums[i]
        #left[i] = total_mul
        #print(result_list[i])
    total_mul = 1
    for i in range(len(nums)-1, -1, -1):
        print(i, result_list[i])
        #right[i] = right[i-1]*nums[i]
        result_list[i] *= total_mul
        total_mul*=nums[i]
    print(result_list)
    return result_list

nums = [1,2,3,4]
productOfArrayWithoutDiv(nums)
