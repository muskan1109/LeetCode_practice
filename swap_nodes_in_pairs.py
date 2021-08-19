# problem #24

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(-1)
        curr = head
        prev = pre_head

        if not curr or not curr.next: return head

        while curr and curr.next:
            temp_next = curr.next.next

            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp_next

            prev = curr
            curr = temp_next

        return pre_head.next