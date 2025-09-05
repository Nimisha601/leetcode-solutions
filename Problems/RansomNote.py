/*
 * @lc app=leetcode id=1760012314 lang=python3
 *
 * RansomNote
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans=[0]*26
        for j in magazine:
            ans[ord(j)-ord('a')]+=1
        for k in ransomNote:
            ans[ord(k)-ord('a')]-=1
        for l in ans:
            if l<0:
                return False
        return True                
        
        