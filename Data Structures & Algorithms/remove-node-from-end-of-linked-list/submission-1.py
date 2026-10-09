# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None
        
        temp = head
        len1 = 0

        while temp:
            

            len1 += 1
            temp = temp.next

        tar =   (len1 - n)-1 
        n = n % len1
        if n == 0:
            return head.next
        temp = head

        for i in range(tar):

            temp = temp.next


        if temp.next:
            temp.next = temp.next.next
        return head
