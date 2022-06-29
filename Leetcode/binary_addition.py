from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #print(a)
        #print(b)
        #while a
        a = list(a)
        b = list(b)
        carr = 0
        res = []
        while a or b or carr:
            if a:
                carr+=int(a.pop())

            if b:
                carr+=int(b.pop())

            res.append(str(carr%2))
            carr//=2
            print(carr)
        return ''.join(res[::-1])

    def addBinaryBase2(self, a, b) -> str:

        carr = 0
        res = []
        #a = list(reversed(a))
        #b = list(reversed(b))
        while a or b or carr:
            if a:
                carr+=int(a.pop())

            if b:
                carr+=int(b.pop())

            res.append(str(carr%2))
            carr//=-2
            print(carr)
        return ''.join(res[::-1])

    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        M = len(arr1)
        N = len(arr2)
        length = max(M, N)
        arr1.reverse()
        arr2.reverse()
        ans = []

        i = 0
        carry = 0
        while i < length or carry:
            val = carry
            if i < M:
                val += arr1[i]
            if i < N:
                val += arr2[i]

            carry = 0
            if val < 0:
                val = -1 * val
                carry = val

            ans.append(val % 2)
            carry += -1 * (val // 2)

            i += 1

        ans.reverse()
        i = 0
        while i + 1 < len(ans) and ans[i] == 0:
            i += 1

        return ans[i:]

num1 = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
num2 = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]


#print(op)
op = Solution().addNegabinary(num1, num2)
print(op)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(arr1, arr2):
    # write your code in Python 3.6
    lookup = {
            -2: (0, 1),
            -1: (1, 1),
            0: (0, 0),
            1: (1, 0),
            2: (0, -1),
            3: (1, -1),
        }
    carry = 0
    result = []
    arr1.reverse()
    arr2.reverse()
    while len(arr1) > 0 or len(arr2) > 0:
        a = 0
        if len(arr1) > 0:
            a = arr1.pop()
        b = 0
        if len(arr2) > 0:
            b = arr2.pop()
        temp = a + b + carry
        res, carry = lookup[temp]
        result.append(res)

    while carry != 0:
        res, carry = lookup[carry]
        result.append(res)

    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return list(reversed(result[::-1]))

