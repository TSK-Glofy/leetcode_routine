#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list, l2_list = [], []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
    
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        if len(l1_list) < len(l2_list):
            l1_list += [0] * (len(l2_list) - len(l1_list))
        if len(l1_list) > len(l2_list):
            l2_list += [0] * (len(l1_list) - len(l2_list))

        l1_list += [0]      
        for i in range(len(l2_list)):
            l1_list[i] += l2_list[i]
            if l1_list[i] >= 10:
                l1_list[i] -= 10
                l1_list[i + 1] += 1
        
        if l1_list[-1] == 0:
            l1_list = l1_list[:-1]

        l1 = ListNode(l1_list[0])
        curr = l1
        for i in l1_list[1:]:
            curr.next = ListNode(i)
            curr = curr.next

        return l1
                    
# @lc code=end

