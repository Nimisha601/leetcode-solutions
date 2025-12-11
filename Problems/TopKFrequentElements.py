/*
 * @lc app=leetcode id=1822460408 lang=python3
 *
 * TopKFrequentElements
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has={}
        for i in range(len(nums)):
            if nums[i] not in has:
                has[nums[i]]=1
            else:
                has[nums[i]]+=1
        ans=[]
        
        han=sorted(has.items(),key = lambda items:items[1],reverse =True)
        for i in range(k):
            ans.append(han[i][0])
        return ans                    

        