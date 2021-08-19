# problem #22

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(open_remain, close_remain, s):
            if open_remain == 0 and close_remain == 0:
                ans.append(s)
            if close_remain > open_remain and close_remain > 0:
                helper(open_remain, close_remain - 1, s+')')
            if open_remain > 0:
                helper(open_remain - 1, close_remain, s+'(')
        ans = []
        helper(n, n, '')
        return ans