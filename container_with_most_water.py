# problem #11

class Solution:
    def maxArea(self, height: List[int]) -> int:
        r, l = len(height) - 1, 0
        ans = float('-inf')

        while r > l:
            ans = max(ans, (r - l) * min(height[r], height[l]))
            if height[r] > height[l]:
                l = l + 1
            else:
                r = r - 1
        return ans  