/*
 * @lc app=leetcode id=1796702169 lang=python3
 *
 * MinimumCostToMakeAtLeastOneValidPathInAGrid
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dire={1:[0,1],
             2:[0,-1],
             3:[1,0],
             4:[-1,0]}
        row,col = len(grid),len(grid[0])
        q=deque([(0,0,0)]) # r, c,cost
        mih={(0,0):0}
        while q:
            r,c,cost = q.popleft()
            if r==row-1 and c==col-1:
                return cost 
            for d in dire:
                dr,dc=dire[d]
                nr,nc= r+dr , c+dc
                n_cost = cost if d==grid[r][c] else  cost+1

                if nr<0 or nc< 0 or nr== row or nc==col or n_cost>=mih.get((nr,nc),float('inf')):
                    continue
                mih[(nr,nc)]= n_cost    
                if d==grid[r][c]:
                    q.appendleft((nr,nc,n_cost))
                else:
                    q.append((nr,nc,n_cost))                 
                