class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue=-1
        maxIndex= 0 
        for i in range(len(arr)-1, -1, -1):
            currentMaxValue = max(maxValue, arr[i])
            arr[i] = maxValue
            maxValue = currentMaxValue
        return arr