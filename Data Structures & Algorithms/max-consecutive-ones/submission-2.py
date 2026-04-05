class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxCounter= 0
        for i in range(len(nums)):
            counter = counter + 1 if nums[i] else 0
            maxCounter = max(maxCounter, counter)
        return maxCounter