# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        c = 0
        while ptr!=None:
            c+=1
            ptr = ptr.next
        

        idx = 0
        if c%2 ==0:
            idx = c//2 + 1
        elif c%2 != 0:
            idx = c //2 + 1
        
        ptr = head
        c=0
        return_ptr = None
        while ptr !=None:
            c+=1
            if c==idx:
                return_ptr = ptr
                break
            else:
                ptr = ptr.next
        
        return return_ptr
        

