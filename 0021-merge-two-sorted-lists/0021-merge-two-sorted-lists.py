# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        return dummy.next


# ------------------------------
# Helper functions to test it
# ------------------------------
def build_linked_list(values):
    """Convert Python list -> Linked list"""
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert Linked list -> Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ------------------------------
# Example Test
# ------------------------------
list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,4])

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print(linked_list_to_list(merged_head))  # Output: [1, 1, 2,]()
