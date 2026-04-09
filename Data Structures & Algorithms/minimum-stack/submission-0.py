class MinStack:

    def __init__(self):
        self.values = []
        self.minValue = 2^31
        self.length = 0
        self.orderedValuesStack = []
        
    def push(self, val: int) -> None:
        self.values.append(val)
        minValue = min(self.orderedValuesStack[-1] if self.orderedValuesStack else val, self.values[-1])
        self.orderedValuesStack.append(minValue)

    def pop(self) -> None:
        self.values.pop()
        self.orderedValuesStack.pop()



    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.orderedValuesStack[-1]


        
