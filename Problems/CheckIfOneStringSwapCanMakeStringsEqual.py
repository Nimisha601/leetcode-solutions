/*
 * @lc app=leetcode id=1761274401 lang=python3
 *
 * CheckIfOneStringSwapCanMakeStringsEqual
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        swap = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap.append(i)
                if len(swap) > 2:
                    return False  # more than 2 mismatches

        if len(swap) != 2:
            return False

        i, j = swap
        return s1[i] == s2[j] and s1[j] == s2[i]


        