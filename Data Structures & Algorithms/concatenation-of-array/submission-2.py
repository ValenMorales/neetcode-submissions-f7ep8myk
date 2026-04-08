class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [nums[0]] * (len(nums) * 2)

        for i in range (len(nums)):
            if i != 0 or i != (len(nums) -1):
                ans[i] = nums[i]
                ans[i+ (len(nums))] = nums[i]
        return ans