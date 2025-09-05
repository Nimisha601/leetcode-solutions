/*
 * @lc app=leetcode id=1759963693 lang=python3
 *
 * FindTheIndexOfTheFirstOccurrenceInAString
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        def l(needle):
            n=len(needle)
            lps=[0]*n
            j=0
            i=1
            while i<n:
                if needle[i]==needle[j]:
                    j+=1
                    lps[i]=j
                    i+=1
                else:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        lps[i]=0
                        i+=1        
            return lps
        def kmp(haystack,needle):
            m=len(needle)
            n=len(haystack)
            lps=l(needle)
            i=j=0 
            while i<n:
                if haystack[i]==needle[j]:
                    i+=1
                    j+=1   
                    if m==j:
                        return i-j
                else :
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1            
            return -1
        return kmp(haystack,needle)