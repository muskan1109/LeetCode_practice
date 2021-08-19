# problem #39

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        ans = []
        first = 0
        total = 0

        candidates.sort()

        memo = {}
        for i, num in enumerate(candidates):
            memo[num] = i

        while True:
            if total == target:
                answer.append(ans[:])
            if total >= target or first >= len(candidates):
                if not ans:
                    return answer
                num = ans.pop()
                first = memo[num] + 1
                total -= num
            else:
                ans.append(candidates[first])
                total += candidates[first]