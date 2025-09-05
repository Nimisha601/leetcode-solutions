/*
 * @lc app=leetcode id=1760000546 lang=python3
 *
 * FirstUniqueCharacterInAString
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=[0]*26
        for i in s:
            ans[ord(i)-ord('a')]+=1
        for j,k in enumerate(s):
             if ans[ord(k)-ord('a')]==1:
                return j
        return -1           
        