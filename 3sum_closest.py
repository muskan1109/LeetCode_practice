# problem #16

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        N = len(nums)
        
        nums.sort()
        
        for i in range(N):
            l = i + 1
            r = N - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if abs(target - s) < abs(target - ans): ans = s
                
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s
        
        return ans