#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_set = len(nums)
        if len_set == 0:
            return 0
        
        hash_set = {}
        res = []
        for i in range(len_set):
            hash_set[nums[i]] = i
        for i in hash_set:
            cnt = 1
            j = i
            if (i - 1) not in hash_set:
                while j + 1 in hash_set:
                    cnt += 1
                    j += 1
                res.append(cnt)
        return max(res)
                       
# @lc code=end

