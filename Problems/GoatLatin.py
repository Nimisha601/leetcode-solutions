/*
 * @lc app=leetcode id=1760349103 lang=python3
 *
 * GoatLatin
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("AEIOUaeiou")
        words = sentence.split()     
        x = len(words)

        for i in range(x):            
            w = words[i]
            if w[0] in vowels:
                words[i] = w + "ma" + "a" * (i + 1)
            else:
                words[i] = w[1:] + w[0] + "ma" + "a" * (i + 1)

        return " ".join(words)
  

        