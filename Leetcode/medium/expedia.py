nums = [1,2,9,1,2,3,1,4,1,5,7]
print(sorted(set(nums)))


def mystery(a, b):
    x = a
    y = b
    while x!=y:
        if x>y:
            x=x-y
        if x<y:
            y=y-x
    print(x, y)
    return x

temp = mystery(2437, 875)
#print(temp)

#str = "abaasass"

from typing import List
def compress(chars: str) -> str:
    print(chars)
    res = {}
    return_str = ""
    if len(chars) == 1:
        return chars

    curr = chars[0]
    cnt = 1
    temp = []
    for i in range(1, len(chars)):
        if curr == chars[i]:
            cnt += 1
        else:
            temp.append(curr)
            temp.append(cnt)
            return_str+=curr
            if cnt>1:
                return_str += str(cnt)
            curr = chars[i]
            cnt = 1

    temp.append(curr)
    return_str+=curr
    if cnt > 1:
        temp.append(cnt)
        return_str+=str(cnt)

    print(return_str)
    print(temp)
    return return_str

str1 = "abc".split()
str1 = ["a", "b", "a", "a", "s", "a", "s", "s"]
str1 =  "abaasass"
str1 = "abaabbbc"
print(str1)
op = compress(str1)
print(op)

people = 8
groups = 4

"""
public static int nToKGroups(int n, int k) {
		if(n < k) {
			return 0;
		}
		int[][] dp = new int[k+1][n+1];
		for(int i = 1; i <= k; i++) {
			for(int j = i; j <= n; j++) {
                if(i==j) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-i];
                }
			}
		}
		return dp[k][n];
	}
"""
# n groups
def grouping(people, groups):
    if people<groups:
        return 0
    #dp = [[0 for i in range(people)] for j in range(groups)]
    dp = [[0 for i in range(groups + 1)] for j in range(people + 1)]
    #print(dp)

    for i in range(0, people + 1):
        dp[i][1] = 1
    #print(dp)
    dp[0][0] = 1
    for i in range(1, people+1):
        for j in range(2, groups+1):
            if i >=j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i-1][j-1]

    print(dp[people][groups])
    return dp[people][groups]
grouping(7, 3)
grouping(200, 111)
grouping(107, 37)
def countOptions(people, groups):
    # Write your code here

    visited = [[0 for i in range(groups+1)] for _ in range(people+1)]
    for i in range(0, people+1):
        visited[i][1] = 1
    visited[0][0] = 1
    for i in range(1, people+1):
        for j in range(2, groups+1):
            if i>=j:
                visited[i][j]= visited[i-1][j-1] + visited[i][j-1]
            else:
                visited[i][j] = visited[i-1][j-1]
    return visited[people][groups]


def ncr(n, r):
    # Initialize the answer
    ans = 1

    for i in range(1, r + 1):
        # Divide simultaneously by
        # i to avoid overflow
        ans *= (n - r + i)
        ans //= i

    return ans


# Function to return the number of
# ways to distribute N identical
# objects in R distinct objects
def NoOfDistributions(N, R):
    return ncr(N - 1, R - 1)

ret  = NoOfDistributions(200, 111)
print(ret)
from enum import Enum
class Color(Enum):
    red = 1
    green = 2


def calculate(pos, prev, left, k):
    # Base Case
    if (pos == k):
        if (left == 0):
            return 1;
        else:
            return 0;

    # If N is divides completely
    # into less than k groups
    if (left == 0):
        return 0;

    answer = 0;

    # Put all possible values
    # greater equal to prev
    for i in range(prev, left + 1):
        answer += calculate(pos + 1, i,
                            left - i, k);

    return answer;


def calculate(pos, prev, left, k):
    # Base Case
    if (pos == k):
        if (left == 0):
            return 1;
        else:
            return 0;

    # If N is divides completely
    # into less than k groups
    if (left == 0):
        return 0;

    answer = 0;

    # Put all possible values
    # greater equal to prev
    for i in range(prev, left + 1):
        answer += calculate(pos + 1, i,
                            left - i, k);

    return answer;


def countWaystoDivide(n, k):
    return calculate(0, 1, n, k);


# Function to