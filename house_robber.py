class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 0): return 0
        K = [0] * len(nums)
        for i in range(len(nums)):
        	if i == 0:
        		K[i] = nums[0]
        	elif i == 1:
        		K[i] = max(nums[0], nums[1])
        	else:
        		prev_selected = K[i - 1] != K[i - 2] 
        		if prev_selected: 
        			K[i] = max(K[i - 2] + nums[i], K[i - 1])
        		else:
        			K[i] = K[i - 1] + nums[i]
        return K[-1]