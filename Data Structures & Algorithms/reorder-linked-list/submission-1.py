class Solution:
    def reorderList(self, head):
        middle_node = self.findMiddleNode(head)
        dummy = middle_node.next
        middle_node.next = None
        head2 = self.reverseLinkedList(dummy)
        head = self.mergeTwoLL(head, head2)
        
        
    def findMiddleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # 1 2 3
    # head: 1, 2, 3, None
    # ntt: 2, 3, None
    # new_next: None, 1, 2, 3
    def reverseLinkedList(self, head):
        new_next = None
        while head:
            next_to_traverse = head.next
            head.next = new_next
            new_next = head
            head = next_to_traverse
        return new_next
    
    def mergeTwoLL(self, l1, l2):
        current = ListNode(-1)
        dummy = current
        
        while l1 and l2:
            current.next = l1
            l1 = l1.next
            current = current.next
            
            current.next = l2
            l2 = l2.next
            current = current.next

            
        current.next = l1 or l2
        
        return dummy.next