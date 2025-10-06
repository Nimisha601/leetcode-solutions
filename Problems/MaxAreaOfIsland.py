/*
 * @lc app=leetcode id=1793247452 lang=python3
 *
 * MaxAreaOfIsland
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m=len(grid[0])
        dire=[[0,1],[1,0],[0,-1],[-1,0]]
        visit= set()
        def bfs(r,c):
            
            visit.add((r,c))
            q= deque([(r,c)])
            box=1
            while q:
                ro,co = q.popleft()
                for dr,dc in dire:
                        nr=ro+dr
                        nc=co+dc
                        if nr<0 or nc<0 or nr>=n or nc>=m or grid[nr][nc]!=1 or (nr,nc) in visit:
                            continue
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        box+=1    
            return box 
        a=0   
        for i in  range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans= bfs(i,j)
                    a=max(ans,a)
        return a            