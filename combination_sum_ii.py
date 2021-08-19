# problem #40

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, target, path):
            if target < 0:
                return
            elif target == 0:
                opt.append(path)
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]: 
                        continue
                    num = candidates[i]
                    dfs(i + 1, target - num, path+[num])
        opt = []
        candidates.sort()
        dfs(0, target, [])
        return opt
        