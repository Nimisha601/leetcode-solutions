/*
 * @lc app=leetcode id=1754680802 lang=python
 *
 * PlusOne
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        y= len(digits)-1
        if(digits[y]==9):
           while(digits[y]==9):
                digits[y]=0
                if y==0:
                    digits.insert(0,1) 
                elif digits[y-1]!=9: 
                    digits[y-1]+=1
                    break
                else: pass    
                y=y-1
        else:
            digits[y]+=1
        return digits                
                
