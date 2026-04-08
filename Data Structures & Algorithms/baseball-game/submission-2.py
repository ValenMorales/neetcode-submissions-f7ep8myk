class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = 0 
        recordsHistory = []
        for i in range(len(operations)):
            match operations[i]:
                case '+':
                        value = (recordsHistory[-1] + recordsHistory[-2])
                        records += value
                        recordsHistory.append(value)
                case 'D':
                        value= recordsHistory[-1] * 2
                        records += value
                        recordsHistory.append(value)
                case 'C':
                        records -= recordsHistory[-1]
                        recordsHistory.pop()
                case _:
                    records += int(operations[i])
                    recordsHistory.append(int(operations[i]))
        return records 

