# problem #77

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(first, combination):
            if len(combination) == k:
                answer.append(combination)
            else:
                for num in range(first, n + 1):
                    helper(num + 1, combination+[num])
        answer = []
        helper(1, [])
        return answer