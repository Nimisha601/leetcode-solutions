/*
 * @lc app=leetcode id=1796621964 lang=python3
 *
 * MinimumObstacleRemovalToReachCorner
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols = len(grid[0])
        min_heap= [(0,0,0)]# obstacles, r,c
        visit=set([(0,0)])
        while min_heap:
            ob,r,c=heapq.heappop(min_heap)
            
            if r==rows-1 and c== cols-1:
                return ob
            nei =[[r+1,c],[r-1,c],[r,c-1],[r,c+1]]
            for dr,dc in nei:
                if dr<0 or dc<0 or dr==rows or dc==cols or (dr,dc) in visit:
                    continue
                heapq.heappush(min_heap,(ob+grid[dr][dc],dr,dc)) 
                visit.add((dr,dc))       

        