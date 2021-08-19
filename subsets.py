# problem #78

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for n in nums:
            new_subs = []
            for sub in answer:
                new_subs.append(sub+[n])
            answer.extend(new_subs)
        return answer