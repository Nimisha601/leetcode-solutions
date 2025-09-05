/*
 * @lc app=leetcode id=1759750050 lang=python3
 *
 * ReverseString
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j: 
           s[i], s[j] = s[j], s[i]
           i += 1
           j -= 1

        
        