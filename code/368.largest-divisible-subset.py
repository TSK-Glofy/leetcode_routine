#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums_len = len(nums)
        dp = [1] * nums_len
        prev = [-1] * nums_len
        dp_len = 0
        i_max = -1
        res = []

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if (nums[j] % nums[i] == 0) and (dp[j] < dp[i] + 1):
                    dp[j] = dp[i] + 1
                    prev[j] = i
            
            if dp_len < dp[i]:
                dp_len = dp[i]
                i_max = i
        j = i_max
        while (j != -1):    
            res.append(nums[j])
            j = prev[j]
        
        res.reverse()
        return res
       
# @lc code=end

