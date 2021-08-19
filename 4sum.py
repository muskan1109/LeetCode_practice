# problem #18

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = set()
        
        for a in range(N):
            for b in range( a + 1, N):
                c = b + 1
                d = N - 1
                
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
                        d -= 1
                        c += 1
        return ans