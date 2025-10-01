/*
 * @lc app=leetcode id=1786829069 lang=python3
 *
 * EvaluateDivision
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        for i in range(len(equations)):
            a,b=equations[i]
            v=values[i]
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append((b,v))
            graph[b].append((a,1/v))
        def bfs(src,dest):
            if src not in graph or dest not in graph :
                return -1
            q=deque()
            visit =set()
            q.append([src,1])
            while q:
                n, w =q.popleft()
                visit.add(n)
                if n == dest:
                    return w
                for nei,weight in graph[n]:
                    if nei not in visit:
                        q.append([nei,w*weight])
                        visit.add(nei)
            return -1          
        ans=[]
        for i,j in queries:
             ans.append(bfs(i,j))
        return ans     

