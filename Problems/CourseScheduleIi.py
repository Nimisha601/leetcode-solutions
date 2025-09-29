/*
 * @lc app=leetcode id=1776766946 lang=python3
 *
 * CourseScheduleIi
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[]for i in range(numCourses)}
        ans=[]
        for i , j in prerequisites:
            graph[i].append(j)
        visit =set()
        def dfs(i):
            if i in visit:
                return False
            if graph[i]==[]:
                if i not in ans:
                    ans.append(i)
                return True
            visit.add(i)

            for k in graph[i]:
                if not dfs(k):
                    return False
            visit.remove(i)
            graph[i]=[]
            ans.append(i)
            return True            
        for l in range(numCourses):
            if not dfs(l):
                return []
        return ans         
        