from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        print(chars)
        res = {}
        if len(chars) == 1:
            return 1

        #for i in chars:
        curr = chars[0]
        cnt = 1
        temp = []
        for i in range(1, len(chars)):
            if curr == chars[i]:
                cnt += 1
            else:
                temp.append(curr)
                temp.append(cnt)
                curr = chars[i]
                cnt = 1

        temp.append(curr)
        if cnt > 1:
            temp.append(cnt)
        print(temp)
        return len(temp)


ip = ["a", "a", "b", "b", "c", "c", "c"]
ip = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ip = ["a"]
ip =  ["a","a","b","b","c","c","c"]
ip = ""
res = Solution().compress(ip)
print(res)
