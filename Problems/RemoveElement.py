/*
 * @lc app=leetcode id=1822263316 lang=python3
 *
 * RemoveElement
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            else:
                continue
        return i                
        