/*
 * @lc app=leetcode id=1787990113 lang=python3
 *
 * PathWithMaximumProbability
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph={}
        for i in range(n):
            graph[i]=[]
        for j in range(len(edges)):
            src,des = edges[j]
            graph[src].append([des,succProb[j]])
            graph[des].append([src,succProb[j]])
        maxh=[(-1,start_node)]
        visit=set()
        while maxh:
            pro,node=heapq.heappop(maxh)
            visit.add(node)
            if node == end_node:
                return pro*-1
            for nei ,prob2 in graph[node]:
                if nei not in visit:
                    heapq.heappush(maxh,(prob2*pro,nei))
        return 0            


        