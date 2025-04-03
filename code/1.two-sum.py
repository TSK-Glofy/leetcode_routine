#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_table:
                return [nums_table[complement], i]
            else:
                nums_table[num] = i
       
# @lc code=end

