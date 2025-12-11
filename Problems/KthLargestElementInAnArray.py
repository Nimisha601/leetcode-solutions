/*
 * @lc app=leetcode id=1851997346 lang=python3
 *
 * KthLargestElementInAnArray
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return heapq.heappop(nums)    
        
        