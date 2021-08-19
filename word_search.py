# problem #79

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_neighbor(i, j):
            opt = []
            if i + 1 < M:
                opt.append((i + 1, j))
            if j + 1 < N: 
                opt.append((i, j + 1))
            if i - 1 >= 0: 
                opt.append((i - 1, j))
            if j - 1 >= 0: 
                opt.append((i, j-1))
            return opt

        def dfs(i, j, l, visited):
            if l == len(word) - 1:
                return True
            visited.add((i, j))
            for ni, nj in get_neighbor(i, j):
                if (ni, nj) not in visited and board[ni][nj] == word[l + 1]:
                    if dfs(ni, nj, l + 1, visited.copy()): 
                        return True
            return False

        M = len(board)
        N = len(board[0])

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()): 
                        return True
        return False