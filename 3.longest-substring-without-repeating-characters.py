#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        count = 0
        max_len = 0

        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            count = right - left + 1
            max_len = max(max_len, count)

        return max_len

        
# @lc code=end

