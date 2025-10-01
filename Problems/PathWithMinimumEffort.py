/*
 * @lc app=leetcode id=1788071503 lang=python3
 *
 * PathWithMinimumEffort
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col = len(heights[0])
        direct=[[0,1],[1,0],[0,-1],[-1,0]]
        minheap=[[0,0,0]]#(diff,r,c)
        visit=set()
        while minheap:
            diff,r,c=heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))    
            if r == row-1 and c ==col-1:
                return diff
            for dr ,dc in direct:
                nr=r+dr
                nc=c+dc 
                if nr<0 or nc<0 or nr>row-1 or nc>col-1 or(nr,nc) in visit:
                    continue
                newdiff=max(diff,abs(heights[r][c]-heights[nr][nc]))  
                heapq.heappush(minheap,(newdiff,nr,nc))     
            

        