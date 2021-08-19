# problem #33

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1
        while True:
            m = (l + r) // 2

            left_num = nums[l]
            right_num = nums[r]
            mid_num = nums[m]

            if left_num == target:
                return l
            if right_num == target:
                return r
            if mid_num == target:
                return m


            if left_num < target and target < mid_num:
                r = m - 1
                continue

            if mid_num < target and target < right_num:
                l = m + 1
                continue
                
            if mid_num > right_num:
                l = m+1
                continue

            if mid_num < left_num:
                r = m - 1
                continue

            return -1