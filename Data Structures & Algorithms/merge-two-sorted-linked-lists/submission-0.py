class Solution:
        def mergeTwoLists(self, list1, list2):
            if not list1 or not list2:
                return list2 if not list1 else list1

            curr = None
            if list1.val < list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            
            head = curr
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                    
            while list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            while list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            
            return head