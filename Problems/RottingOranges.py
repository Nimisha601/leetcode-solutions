/*
 * @lc app=leetcode id=1775927052 lang=python3
 *
 * RottingOranges
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

from collections import deque
class Solution:
  def orangesRotting(self,grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    t=0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, t))  
            elif grid[r][c] == 1:
                fresh += 1
    while queue:
        r, c, t = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                queue.append((nr, nc, t + 1))
                grid[nr][nc] = 2
                fresh -= 1
    
    return t if fresh == 0 else -1

        