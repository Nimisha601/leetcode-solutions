/*
 * @lc app=leetcode id=1761232055 lang=python3
 *
 * PermutationInString
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        ans1=[0]*26
        ans2=[0]*26
        for i in s1:
            ans1[ord(i)-ord('a')]+=1
        for j in s2[:len(s1)]:
            ans2[ord(j)-ord('a')]+=1
        if ans1==ans2:
            return True
        for m in range(len(s1),len(s2)):
            ans2[ord(s2[m])-ord('a')]+=1
            ans2[ord(s2[m-len(s1)])-ord('a')]-=1
            if ans1==ans2:
                return True
            
        return False            
            
        
        