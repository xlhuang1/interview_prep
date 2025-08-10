# You are given a 2D grid of characters and a word. Return True if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically). The same letter cell may not be used more than once.

from typing import List

def exist(board: List[List[str]], word: str) -> bool:

    def dfs_from_cell(r, c, word_idx, visited):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L, R, U, D

        if word_idx == len(word):
            # will return True meaning word found
            return True

        if word[word_idx] == board[r][c]:
            visited.add((r, c))
            for dir in directions:
                if 0 <= r + dir[0] < len(board) and (0 <= c + dir[1] < len(board[0])):
                    next_r, next_c = r+dir[0], c+dir[1]
                    if (next_r, next_c) not in visited:
                        if dfs_from_cell(next_r, next_c, word_idx + 1, visited):
                            return True
            visited.remove((r, c))
        return False


    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == word[0]:
                if dfs_from_cell(r, c, 0, set()):
                    return True
    return False
