# problem #74

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        A = []
        for row in matrix: 
            A.extend(row)

        l = 0
        r = len(A) - 1
        while l <= r:
            m = (l + r) // 2
            if A[l] == target: 
                return True
            if A[m] == target: 
                return True
            if A[r] == target: 
                return True

            if A[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False