# problem #15

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        N = len(nums)
        
        for i in range(N):
            j = i + 1
            k = N - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    k -= 1
                    j += 1
                    
        return ans