/*
 * @lc app=leetcode id=1760919568 lang=python3
 *
 * LongestSubstringWithoutRepeatingCharacters
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        ans=[]
        for i in range(len(s)):
            if s[i] in ans:
                ans=ans[ans.index(s[i])+1:]
            ans.append(s[i])
            m=max(m,len(ans))
                
        return m