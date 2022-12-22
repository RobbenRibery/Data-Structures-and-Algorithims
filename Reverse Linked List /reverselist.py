#Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = None

        def recursive(head: Optional[ListNode], res): 

            if head == None: 
                return ListNode(val = '')
            else:
                if head.next == None: 
                    return ListNode(val = head.val, next = res)
                else: 
                    if not res: 
                        res = ListNode(val=head.val, next = None)
                    else:
                        res = ListNode(val=head.val, next = res)
                    print(res.val, res.next)
                    return recursive(head.next, res)

        return recursive(head,res)


if __name__ == "__main__": 

    head = [5,4,3,2,1]
    s = Solution()

    print(s.reverseList(
        head = head 
    ))

