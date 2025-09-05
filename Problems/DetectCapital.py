/*
 * @lc app=leetcode id=1760327017 lang=python3
 *
 * DetectCapital
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        if n==1:
            return True
        if  ord('A')<=ord(word[0])<=ord('Z') and  ord('a')<=ord(word[1])<=ord('z'):
            for i in range(1,len(word)):
                if not(ord('a')<=ord(word[i])<=ord('z')):
                   return False
        elif  ord('a')<=ord(word[0])<=ord('z'):
            for k in range(1,len(word)):
                if not (ord('a')<=ord(word[k])<=ord('z')):
                  return False
        else :
            for j in range(1,len(word)):
                if not(ord('A')<=ord(word[j])<=ord('Z')):
                    return False              
        return True
                    