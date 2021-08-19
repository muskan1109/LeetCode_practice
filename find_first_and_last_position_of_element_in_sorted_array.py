# problem #34

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        l = 0
        r = len(nums)
        p = (l + r) // 2

        while nums[p] != target:
            if nums[p] > target: 
                r = p
            else: 
                l = p

            p_next = (l + r) // 2
            if p == p_next: 
                return [-1, -1]
            p = p_next

        l = r = p
        
        while r + 1 < len(nums) and nums[r + 1] == target:
            r = r + 1
        while 0 <= l - 1 and nums[l - 1] == target:
            l = l - 1
        return [l, r]