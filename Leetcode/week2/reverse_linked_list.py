# Definition for singly-linked list.
from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if not head:
            return None
        while head.next is not None:
            stack.append(head.val)
            head = head.next
        stack.append(head.val)
        print(stack)
        head = None
        first_node = None
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

            if head is None:
                head = ListNode(stack[i], None)
                first_node = head
            else:
                curr_head = ListNode(stack[i], None)
                head.next = curr_head
                head = head.next
        return first_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        prev = None
        next_val = head.next
        while curr.next is not None:
            #print(curr.val)
            temp = curr.next
            #temp.next = prev
            #prev = next_val
            #curr = next_val
            #curr = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #print(head.val)
        while prev.next is not None:
            print(prev.val)
            prev = prev.next
        #print(curr.val, curr.next.val)




nums = [1,2,3,4,5]



my_val = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
Solution().reverseList(my_val)
