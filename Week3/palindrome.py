# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #two pointer fast slow approach
        slow = head
        fast = head
        array = []
        while fast and fast.next is not None:
            array.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        #now slow is at middle, having one half of the palindrome
        i = len(array)
        while i != 0:
            if array[i-1] != slow.val:
                return False
            else:
                i -= 1
                slow = slow.next
        return True 