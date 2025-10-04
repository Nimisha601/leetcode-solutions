/*
 * @lc app=leetcode id=1790932349 lang=python3
 *
 * ShortestPathInBinaryMatrix
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bound(r,c):
            if r<0 or c<0 or c> l-1 or r>l-1 :
                return False
            return True 
        if grid[0][0]==1:
            return -1       
        l= len(grid)
        q=deque([(0,0,1)])# row , col , box
        visit = set()
        
        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1],[1,1],[-1,-1]]
        while q:
            r, c, box = q.popleft()
            if r ==l-1 and c == l-1 :
                return box 
           
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if bound(nr,nc) and grid[nr][nc]==0 and (nr,nc) not in visit :
                    q.append((nr,nc,box+1))
                    visit.add((nr,nc))
        return -1
        