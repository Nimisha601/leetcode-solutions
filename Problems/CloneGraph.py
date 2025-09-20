/*
 * @lc app=leetcode id=1776097197 lang=python3
 *
 * CloneGraph
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        has={}
        def dfs(node):
    
         if node in has:
            return has[node]
         copy = Node(node.val)
         has[node]=copy 
         for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
         return copy
        return dfs(node)if node else None     
