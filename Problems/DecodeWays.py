/*
 * @lc app=leetcode id=1761745696 lang=python3
 *
 * DecodeWays
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
 def numDecodings(self, s: str) -> int:
       
    if not s or s[0] == '0':
        return 0

    prev2 = 1  
    prev1=1        

    for i in range(1, len(s)):
        cur = 0
        # one-digit
        if s[i] != '0':
            cur += prev1
        # two-digit
        two = int(s[i-1:i+1])
        if 10 <= two <= 26:
            cur += prev2

        prev2, prev1 = prev1, cur

        if prev1 == 0:  
            
            pass

    return prev1
