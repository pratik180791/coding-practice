class MaxHeap:
    def __init__(self, arr=[]):
        self.heap = []

        if arr:
            for i in arr:
                self.push(i)

    def push(self, value):
        self.heap.append(value)
        self.bottom_up(len(self.heap)-1)

    def bottom_up(self, index):
        root_index = (index-1)//2 #pivot
        if root_index < 0:
            return
        if self.heap[index] > self.heap[root_index]:
            self.swap(index, root_index)
            self.bottom_up(root_index)

    def top_down(self, index):
        child_index = 2*index+1
        if child_index>=len(self.heap):
            return
        if child_index+1 < len(self.heap) and self.heap[child_index]<self.heap[child_index+1]:
            child_index+=1
        if self.heap[child_index] > self.heap[index]:
            self.swap(child_index, index)
            self.top_down(child_index)

    def swap(self, left, right):
        self.heap[left], self.heap[right] = self.heap[right], self.heap[left]

    def peek(self):
        if len(self.heap)>=0:
            return self.heap[0]
        return "Empty Heap"


m= MaxHeap([1,2,3,4,5,6])
print(m.peek())
m.push(1)
m.push(11)
print(m.peek())
print(m.heap)
