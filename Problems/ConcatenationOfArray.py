/*
 * @lc app=leetcode id=1822253463 lang=python3
 *
 * ConcatenationOfArray
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans        

        