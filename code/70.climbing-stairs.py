#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n >= 3:
            for i in range(3, n + 1):
                dp.append(dp[i-1] + dp[i-2])
            return dp[n]
          
# @lc code=end

