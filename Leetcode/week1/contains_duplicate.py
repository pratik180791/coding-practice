from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupes = {}

        for i in nums:
            present_val = dupes.get(i, 0)
            present_val += 1
            if present_val >= 2:
                return True
            dupes[i] = 1
        return False
    