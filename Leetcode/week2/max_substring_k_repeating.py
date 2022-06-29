sub = "eceba"
k = 2

s = "abcabcbb"
op = 3
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        end = 0

        curr_str = start
        visited = {}
        max_len = -1
        while end < len(s):
            #print(visited)
            right_char = s[end]
            visited.update({right_char: visited.get(right_char, 0)+1})

            while len(visited.keys())>k:
                left_char = s[start]
                visited.update({left_char: visited.get(left_char, 0)-1})
                if visited.get(left_char, 0) == 0:
                    visited.pop(left_char)

                start+=1
            max_len = max(max_len, end-start+1)
            end+=1
            #print(end)
        return max_len


    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        visited = {}
        max_len = -100
        while end<len(s):
            print(end, visited, s[end], start)
            if s[end] in visited and start <= visited[s[end]]:
                start = visited[s[end]]+1
                #visited.pop(s[end])
                visited.update({s[end]: end})
            else:
                visited.update({s[end]: end})
                max_len = max(max_len, end-start+1)
            end+=1
        return max_len
s = "pwwkew"
#s = "bbbbb"
#s = "abcabcbb"
my_op = Solution().lengthOfLongestSubstring(s)
print(my_op)
#my_op = Solution().lengthOfLongestSubstringKDistinct(sub, k)
#print(my_op)