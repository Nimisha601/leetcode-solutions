/*
 * @lc app=leetcode id=1761456181 lang=python3
 *
 * RemoveAllAdjacentDuplicatesInStringIi
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        for i in s:
            if stack and stack[-1][0]==i:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([i,1])

        return"".join(c*cnt for c,cnt in stack)                    

