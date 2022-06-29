class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        def swap(a, i, j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            return a

        if not s:
            return s
        temp = list(s)
        i, j = 0, len(s)-1
        while i<j:
            swap(temp, i, j)
            i+=1
            j-=1
        return "".join(temp)

ip = "pratik"
a = Solution().reverseString(ip)
print(a)