/*
 * @lc app=leetcode id=1760576605 lang=python3
 *
 * ShuffleString
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans =[""]*len(s)
        for i in range(len(s)):
            ans[indices[i]]=s[i]
        return"".join(ans)    
        