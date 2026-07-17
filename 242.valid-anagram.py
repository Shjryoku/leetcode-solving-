#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = {}

        for a in s:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
                 
        for b in t:
            if b in d:
                d[b] -= 1
                if d[b] == 0:
                    d.pop(b)
                elif d[b] < 0: return False
            else: return False
        
        return not d

# @lc code=end

