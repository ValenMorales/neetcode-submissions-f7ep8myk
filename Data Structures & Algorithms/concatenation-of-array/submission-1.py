import numpy as np
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_array = np.array(nums)
        ans = np.concatenate((nums_array, nums_array))
        return ans.tolist()