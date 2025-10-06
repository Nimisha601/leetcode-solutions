/*
 * @lc app=leetcode id=1793206755 lang=python3
 *
 * NetworkDelayTime
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph ={i:[] for i in range(1,n+1)}
        for j in range(len(times)):
            u,v,t = times[j]
            graph[u].append((v,t))
       
        minh= [(0,k)]# time,node
        visit=set()
        t=0
        while minh:
            time,node = heapq.heappop(minh)
            if node in visit:
                continue
            visit.add(node) 
            t=max(t,time)   
            for nei,t2 in graph[node]:
                if nei not in visit:
                    nt = time+t2
                    heapq.heappush(minh,(nt,nei))    
        return t if len(visit)== n else -1