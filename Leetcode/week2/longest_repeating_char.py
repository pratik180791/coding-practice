class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        end = 0
        start = 0
        max_len = -1
        for end, _ in enumerate(s):
            curr_right_char = s[end]
            curr_left_char = s[start]
            if curr_right_char not in mapper:
                mapper[curr_right_char] = 0

            mapper[curr_right_char] += 1
            curr_len = (end-start)+1
            max_frequency = max(mapper.values())

            if curr_len-max_frequency<=k:
                max_len = max(curr_len, max_len)
            else:
                mapper[curr_left_char]-=1
                if not mapper[curr_left_char]:
                    mapper.pop(curr_left_char)
                start+=1
        return max_len


s = "ABAB"
s = "CABAAAABBBBBA"
k = 2
op = Solution().characterReplacement(s, k)
print(op)