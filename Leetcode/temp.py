class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.cnt = 0
        self.ma = size
        self.ds = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.ds.append(val)
        self.cnt += 1
        ds_len = len(self.ds)

        if ds_len < self.ma:
            #print("HERE")
            #print(sum(self.ds[::1]))
            #print(self.ma)
            return sum(self.ds[::1]) / ds_len
        else:
            sum_a = sum(self.ds[ds_len - self.ma:ds_len]) / self.ma
            print(sum_a)
            return sum_a

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val) new
movingAverage=MovingAverage(3)
ma = movingAverage.next(1) #// return 1.0 = 1 / 1
print(ma)
ma = movingAverage.next(10) #// return 5.5 = (1 + 10) / 2
print(ma)
ma = movingAverage.next(3) #// return 4.66667 = (1 + 10 + 3) / 3
print(ma)
ma = movingAverage.next(5) #// return 6.0 = (10 + 3 + 5) / 3
print(ma)
