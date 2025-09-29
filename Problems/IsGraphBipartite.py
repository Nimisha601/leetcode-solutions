/*
 * @lc app=leetcode id=1785334129 lang=python3
 *
 * IsGraphBipartite
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v= len(graph)
        ans=[0]*v
        def bfs(i):
            if ans[i]:
                return True
            q=deque([i])
            ans[i]=-1
            while q:
                i=q.popleft()
                for nei in graph[i]:
                    if ans[nei]==ans[i]:
                        return False 
                    elif not ans[nei]:
                        q.append(nei)
                        ans[nei]=-1*ans[i]
            return True                    
        for i in range(v):
            if not bfs(i):
                return False
        return True        
        