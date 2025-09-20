/*
 * @lc app=leetcode id=1776143447 lang=python3
 *
 * NumberOfIslands
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q=deque([(r,c)])
            di=[(0,1),(1,0),(-1,0),(0,-1)]
            while q:
                ro,co=q.popleft()
                for dr, dc in di:
                    rn=ro+dr
                    cn=co+dc
                    if rn in range(row)and cn in range(col)and grid[rn][cn]=="1"and (rn,cn)not in visit:
                        q.append((rn,cn))
                        visit.add((rn,cn))

           
        if not grid:
            return 0
        island =0
        visit=set()
        row ,col = len(grid),len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island               

        