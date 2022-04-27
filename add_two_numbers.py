class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail_l1 = l1
        tail_l2 = l2
        res = None
        add = 0
        while tail_l1 != None and tail_l2 != None:
            sum = tail_l1.val + tail_l2.val
            tail_l1 = tail_l1.next
            tail_l2 = tail_l2.next
            if add:
                sum += 1
            add = sum > 9
            if res == None:
                res = ListNode(sum - 10 if add else sum)
                tail = res
                continue
            tail.next = ListNode(sum - 10 if add else sum)
            tail = tail.next
        tail.next = tail_l1 if tail_l1 != None else tail_l2
        while tail != None and tail.next != None:
            tail = tail.next
            if add:
                if tail.val != 9:
                    tail.val += 1
                    add = 0
                else:
                    tail.val = 0
        if add:
            tail.next = ListNode(1)
        return res