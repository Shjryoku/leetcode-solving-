#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        wasNum = set()

        for n in nums:
            if n in wasNum:
                return True
            wasNum.add(n)
        
        return False





# @lc code=end
