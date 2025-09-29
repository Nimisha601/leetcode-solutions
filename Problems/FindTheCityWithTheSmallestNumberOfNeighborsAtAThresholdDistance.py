/*
 * @lc app=leetcode id=1786261010 lang=python3
 *
 * FindTheCityWithTheSmallestNumberOfNeighborsAtAThresholdDistance
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph ={}
        for i in range(n):
            graph[i]=[]
        for s,d,w in edges:
            graph[s].append([d,w])
            graph[d].append([s,w])
        def dijistra (src):
            heap=[[0,src]]
            visit=set()
            while heap:
                n1,n2=heapq.heappop(heap)
                if n2 in visit:
                    continue
                visit.add(n2)
                for m1,m2 in graph[n2]:
                    if m1 not in visit:
                        if m2+n1<=distanceThreshold:
                            heapq.heappush(heap ,(m2+n1,m1))  
            return len(visit)-1
        res=-1
        mi_count =n    
        for i in range(n):
            count=dijistra(i)
            if count<=mi_count:
                mi_count=count
                res=i    
        return res
        