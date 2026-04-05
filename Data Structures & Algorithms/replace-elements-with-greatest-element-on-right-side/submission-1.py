class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue=0 
        maxIndex= 0 
        for i in range(len(arr)):
            if i+1 < len(arr):
                if maxIndex <= i:
                    maxCurrentValue, maxIndex= self.calculateMax(arr[i:])
                arr[i] = maxCurrentValue
            else:
                arr[i] = -1
        return arr

    def calculateMax(self, arr: List[int]) -> int:
        maxValue=0 
        maxIndex=0
        for i in range(1, len(arr), 1):
            if maxValue < arr[i]:
                maxValue=arr[i]
                maxIndex = i
        return maxValue, maxIndex