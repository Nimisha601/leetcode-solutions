/*
 * @lc app=leetcode id=1761700243 lang=python3
 *
 * MultiplyStrings
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
  def multiply(self, num1: str, num2: str) -> str:
        
    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    res = [0] * (m + n)

    for i in range(m - 1, -1, -1):  # from rightmost digit
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum_ = mul + res[i + j + 1]  # add existing value
            res[i + j + 1] = sum_ % 10   # store the digit
            res[i + j] += sum_ // 10     # carry

    # Convert array to string, skipping leading zeros
    result = "".join(map(str, res)).lstrip("0")
    return result if result else "0"

        