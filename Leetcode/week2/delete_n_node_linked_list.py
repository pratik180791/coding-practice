from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mapper = {}
        cnt = 1

        curr = head
        while curr.next:
            mapper.update({cnt: curr})
            curr = curr.next
            cnt += 1
        total_nodes = cnt
        if total_nodes<=0 and n==total_nodes:
            return None


        temp_curr = curr = head

        while total_nodes != 0:
            print(total_nodes, (cnt - n))
            if total_nodes == (cnt - n):
                print("here")
                target_node = curr.next
                print(curr)
                curr.next = target_node.next
                target_node.next = None
                break
            curr = curr.next
            total_nodes -= 1
            # print(total_nodes, n-1)
        return temp_curr
