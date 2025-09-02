/*
 * @lc app=leetcode id=1756495646 lang=python3
 *
 * IntersectionOfTwoArraysIi
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1={}
        n2={}
        k = []
        for i in nums1:
            n1[i] = n1[i]+1 if i in n1.keys() else 1
        for i in nums2:
            n2[i] = n2[i]+1 if i in n2.keys() else 1
        for i in n1.keys():
            if i in n2.keys():
                x = min(n1[i], n2[i])
            else:
                continue# agar ye nahi lagyega t x banega hi nahi 
                
            for j in range(x):
                k.append(i)
        return k   