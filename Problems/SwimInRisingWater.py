/*
 * @lc app=leetcode id=1793166948 lang=python3
 *
 * SwimInRisingWater
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dire=[[0,1],[1,0],[0,-1],[-1,0]]
        if not grid:
            return 0
        n= len(grid)
        minh=[(grid[0][0],0,0)]# time, r,c
        visit=set()
        visit.add((0,0))
        while minh:
            t,i,j=heapq.heappop(minh)
            if i ==n-1 and j==n-1:
                return t
            for dr,dc in dire :
                r=i+dr
                c=j+dc
                if r<0 or c<0 or r==n or c==n or (r,c) in visit:
                    continue
                tn=max(grid[r][c],t)     
                visit.add((r,c))
                heapq.heappush( minh,(tn,r,c))
                   
