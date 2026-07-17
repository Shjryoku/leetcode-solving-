#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return (left + 1, right + 1)
            if curr > target:
                right -= 1
            elif curr < target:
                left += 1
        
        return 0
        
# @lc code=end

