/*
 * @lc app=leetcode id=1793959445 lang=python3
 *
 * LongestPathWithDifferentAdjacentCharacters
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph={i:[]for i in range(len(parent))}
        for j ,k in  enumerate (parent): 
            if k == -1:
                continue   
            graph[k].append(j)
        ans=1    
        def dfs(node):
           nonlocal ans 
           long1=0
           long2=0

           for nei in graph[node]:
            leng=dfs(nei)
            if s[nei]==s[node]:
                continue
            
            if leng>long1:
                long2=long1
                long1=leng
            elif leng>long2:
                long2=leng
           ans=max(ans,long1+long2+1)
           return long1+1
        dfs(0)
        return ans    
                          





        