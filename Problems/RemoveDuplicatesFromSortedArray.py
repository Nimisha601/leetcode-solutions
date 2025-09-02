/*
 * @lc app=leetcode id=1754688594 lang=python
 *
 * RemoveDuplicatesFromSortedArray
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z= len(nums)
        
        u =0
        k=[]

        for x in range(z):
           if nums[x] not in k:
              k.append(nums[x])
              u+=1
            
            
        for y in range(u):
            nums[y]=k[y]
        return  u

