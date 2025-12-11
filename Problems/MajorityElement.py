/*
 * @lc app=leetcode id=1822272062 lang=python3
 *
 * MajorityElement
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele={}
        for i in range(len(nums)):
            if nums[i] in ele:
                ele[nums[i]]+=1
            else:
                ele[nums[i]]=1
        return max(ele,key=ele.get)            
            

        