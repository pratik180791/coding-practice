def _fibo(n):
    if n in (0, 1):
        return n
    return _fibo(n-2) + _fibo(n-1)

class Solution:
    def fib(self, N) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        print(cache)
        return cache[N]


for i in range(21):
    print(Solution().fib(i))


"""
n = 0 , 0
n = 1, 1
n = 2 , fib(n-1) + fib(n-2) = fib(1) + fib(0) = 1 + 0 = 1
n = 3 = fib(2) + fib(1) = 1+1 = 2
n = 4 = fib(3) + fib(2) = 2+1 = 3  

"""