#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if buy_ptr > prices[i]:
                buy_ptr = prices[i]
            elif res < prices[i] - buy_ptr:
                res = prices[i] - buy_ptr
        
        return res

# @lc code=end

