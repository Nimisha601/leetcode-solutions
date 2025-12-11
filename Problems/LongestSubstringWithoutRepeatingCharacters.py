/*
 * @lc app=leetcode id=1801389084 lang=python3
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
       seen={}
       best=0
       left=0
       for right,i in enumerate(s):
         if i in seen and seen[i]>=left:
            left =seen[i]+1
         seen[i]=right
         best =max(best,right-left+1)
       return best    