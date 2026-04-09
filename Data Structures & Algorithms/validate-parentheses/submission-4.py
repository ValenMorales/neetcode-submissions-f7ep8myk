class Solution:
    def isValid(self, s: str) -> bool:
        pendingValuesList = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                pendingValuesList.append(self.correspondingClosedBracket(s[i]))
            else:
                if len(pendingValuesList) == 0:
                    return False 
                if s[i] == pendingValuesList[-1]:
                    pendingValuesList.pop()
                else:
                    return False
        return len(pendingValuesList) == 0 

    def correspondingClosedBracket(self, value:str) -> str:
        match value:
            case '{':
                return '}'
            case '[':
                return ']'
            case '(':
                return ')'

