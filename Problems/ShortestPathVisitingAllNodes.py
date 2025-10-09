/*
 * @lc app=leetcode id=1794039355 lang=python3
 *
 * ShortestPathVisitingAllNodes
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
      n=len(graph)
      
      q= deque()
      visit=set()
      path=0
      for i in range(n):
        a=(1<<i)
        q.append((i,a,0))
        visit.add((i,a)) 
      full =(1<<n)-1   
      while q:
        node, mask,dist=q.popleft()
        if mask ==full:
            return dist
        
        for nei in graph[node]:
            new=mask|(1<<nei)
            if (nei,new) not in visit:
                visit.add((nei,new))
                q.append((nei,new,dist+1))
      return -1   