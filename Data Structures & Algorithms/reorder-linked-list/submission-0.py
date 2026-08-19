# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1-2-3-4-5
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # STEP1: find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Now: slow is the end of the first half at 3

        # STEP2: reverse the second half
        second = slow.next
        slow.next = prev = None
        while second:
            next_to_process = second.next
            second.next = prev
            prev = second
            second = next_to_process
        # Now: two lists: 'head' is the start of the first list
        # 'prev' is the head of the second list

        # STEP3: merge two lists
        # ll1:  -2-3
        # ll2:  -4
        # res:  1-5-2-4-3
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
