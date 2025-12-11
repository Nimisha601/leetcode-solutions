/*
 * @lc app=leetcode id=1801077634 lang=python3
 *
 * ReconstructItinerary
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())   # pop from end (O(1))
            res.append(airport)

        dfs("JFK")
        return res[::-1]
