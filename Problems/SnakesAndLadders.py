/*
 * @lc app=leetcode id=1786546380 lang=python3
 *
 * SnakesAndLadders
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length=len(board)
        board.reverse()
        def intopos(square):
            r=(square-1)//length
            c=(square-1)%length
            if r%2:
                c=length-1-c
            
            return [r,c]
        q=deque()
        q.append([1,0])#square,moves
        visit=set()
        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                nextsq=square+i
                r,c=intopos(nextsq)
                if board[r][c]!=-1:
                    nextsq=board[r][c]
                if nextsq==length*length:
                    return moves+1
                if nextsq not in visit:
                    visit.add(nextsq)
                    q.append([nextsq,moves+1])
        return -1


        