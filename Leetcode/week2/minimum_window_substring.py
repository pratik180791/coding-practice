import sys
from collections import Counter
class Solution:
    def _minWindow(self, s: str, t: str) -> str:
        start = 0
        all_windows = {}

        t_counter = Counter(t)
        required_len = len(t_counter)

        formed_len = 0

        min_val = sys.maxsize
        min_window = ""
        curr_counter = {}

        for end, _ in enumerate(s):
            #print(curr_counter)
            end_char = s[end]
            curr_counter.update(({end_char: curr_counter.get(end_char, 0)+1}))

            if end_char in t_counter and curr_counter[end_char] == t_counter[end_char]:
                formed_len+=1

            while start<=end and formed_len == required_len:
                print(all_windows)
                window_len = end - start + 1
                all_windows[s[start:end+1]] = window_len
                curr_char = s[start]

                curr_counter[s[start]]-=1
                if curr_char in t_counter and len(curr_counter)<len(t_counter):
                    formed_len-=1
                start+=1
        for i, j in t_counter:
            pass
        for key, val in all_windows.items():
            if val<min_val:
                min_window = key
        print(all_windows)
        return min_window

    def min_window(self,s, t):
        start = 0
        all_windows = {}

        t_counter = Counter(t)
        required_len = len(t_counter)

        formed_len = 0

        min_val = sys.maxsize
        min_window_start = 0
        curr_counter = {}
        for end, end_char in enumerate(s):
            if end_char in t_counter:
                if t_counter[end_char]>0:
                    required_len-=1
                t_counter[end_char]-=1

            while required_len == 0:
                if end-start+1<min_val:
                    min_val = end-start+1
                    min_window_start = start
                if s[start] in t_counter:
                    t_counter[s[start]]+=1
                    if t_counter[s[start]]>0:
                        required_len+=1
                start+=1
        if min_val == sys.maxsize:
            return ""
        return s[min_window_start:min_window_start+min_val]
        #return min_val


s = "ADOBECODEBANC"
#s = "AAB"
t = "ABC"
#s = "bdab"
#t = "ab"
expected_op= "BANC"
op = Solution().min_window(s, t)
print(op)
#op = Solution().minWindow(s, t )
print(op)
