/*
 * @lc app=leetcode id=1715755586 lang=python3
 *
 * 3sum
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans=[]
    n= len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        l=i+1
        h=n-1
        while l<h:
            total =nums[i]+nums[l]+nums[h]
            if total ==0:
                ans.append([nums[i],nums[l],nums[h]])
                
                while l<h and nums[l]==nums[l+1]:
                  l+=1
                while l<h and nums[h]== nums[h-1]:
                  h-=1
                l+=1
                h-=1  
            elif total<0:
                l+=1
            else:
                h-=1
    return ans                 






                


                
        