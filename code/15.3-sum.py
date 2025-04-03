#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        nums_len = len(nums)
        for i in range(nums_len):
            j = i + 1
            k = nums_len - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return list(s)
     
# @lc code=end

