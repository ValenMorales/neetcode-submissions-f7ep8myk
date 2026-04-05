class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxCounter= 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter+=1
                if maxCounter < counter:
                    maxCounter = counter
            else:
                if maxCounter < counter:
                    maxCounter = counter
                counter = 0
        return maxCounter