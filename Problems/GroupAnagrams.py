/*
 * @lc app=leetcode id=1760943959 lang=python3
 *
 * GroupAnagrams
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp={}
        for w in strs:
            cnt=[0]*26
            for i in w:
                cnt[ord(i)-ord('a')]+=1
            key =tuple(cnt)
            if key not in comp:
                comp[key]=[]
            comp[key].append(w)
        return list(comp.values())            
        