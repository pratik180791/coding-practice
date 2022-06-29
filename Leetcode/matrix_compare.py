ip = ["ball","asee","let","lep"]
#ip = ["abcd", "xyz", "ef"]
import itertools
#from itertools import izip_longest as izip
class Solution:
    def validWordSquare(self, words) -> bool:
        #return map(None, *words) == map(None, *map(None, *words))
        #return (transposed = list(itertools.zip_longest(*words))) == list(zip(*transposed))
        f = lambda x: map(None, *x)  # padded Transpose
        return f(f(words)) == f(words)

    def _validWordSquare(self, words) -> bool:
        arr = []
        max_len = -1
        for i in words:
            if len(list(i)) > max_len:
                max_len = len(list(i))
            temp = list(i)
            if len((list(i)))<max_len:
                temp = list(i)+["" for i in range(max_len-len(list(i)))]

            arr.append(temp)

        print(arr)

        rows = len(arr)
        columns = len(arr[0])
        print(columns)
        print(rows)
        res = []

        def column(matrix, i):
            return [row[i] for row in matrix]

        for i in range(columns):
            temp = ""
            res.append("".join(column(arr, i)))
        print(res)
        print(words)
        return res == words

res = Solution().validWordSquare(ip)
print(res)

@staticmethod
def dum():
    pass
