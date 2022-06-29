
class Subarray:
    def __init__(self):
        self.max_len = 0

    def printSubArrays(self, arr, start, end):
        # Stop if we have reached the end of the array
        if end == len(arr):
            return

        # Increment the end point and start from 0
        elif start > end:
            return self.printSubArrays(arr, 0, end + 1)
        else:
            return self.printSubArrays(arr, start + 1, end)


