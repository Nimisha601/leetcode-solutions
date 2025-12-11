/*
 * @lc app=leetcode id=1822279950 lang=python3
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
        #(by using boyer-moore voting algo)
        cand =nums[0]
        count =1 
        for i in range(1,len(nums)):
            if count ==0:
                cand =nums[i]
                count =1 
            elif nums[i]==cand:
                count+=1
            else:
                count-=1
        return cand        


            

        