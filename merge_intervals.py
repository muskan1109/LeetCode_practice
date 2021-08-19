# problem #56

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort() 
        
        for inter in intervals:
            if len(result) > 0 and result[-1][1] >= inter[0]: 
                result[-1][1] = max(result[-1][1], inter[1])
            else: 
                result.append(inter) 
        return result