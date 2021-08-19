# problem #55

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step_need = 0
        for num in reversed(nums[:-1]):
            step_need += 1
            if num >= step_need:
                step_need = 0
        return step_need == 0