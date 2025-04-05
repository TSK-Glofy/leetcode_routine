#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergetwolist(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l2:
            return l1
        if not l1:
            return l2
        
        if l1.val < l2.val:
            l1.next = self.mergetwolist(l1.next, l2)
            return l1
        else:
            l2.next = self.mergetwolist(l1, l2.next)
            return l2

        
    def divide(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
            if left == right:
                return lists[left]
            
            mid = left + (right - left) // 2
            l1 = self.divide(lists, left, mid)
            l2 = self.divide(lists, mid + 1, right)
            return self.mergetwolist(l1,l2)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         if not lists:
              return None
         else:
              return self.divide(lists, 0, len(lists) - 1)
        
# @lc code=end
