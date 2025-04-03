#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(ans):
            if ans == 0:
                return 0
            if ans < 0:
                return float('inf')
            
            res = float('inf')
            for coin in coins:
                res = min(res, solve(ans - coin) + 1)
            return res
        
        res = solve(amount)
        if res != float('inf'):
            return res
        else:
            return -1
       
# @lc code=end

