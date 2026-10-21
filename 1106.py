class Solution:
    stack = []
    def parseOr(self) -> str:
        res = 'f'
        while self.stack[-1] != '|':
            exp = self.stack.pop()
            if exp == 't':
                res = 't'
        return res
    def parseAnd(self) -> str:
        res = 't'
        while self.stack[-1] != '&':
            exp = self.stack.pop()
            if exp == 'f':
                res = 'f'
        return res
    def parseNegate(self) -> str:
        exp = self.stack.pop()
        return 't' if exp == 'f' else 'f'

    def parseBoolExpr(self, expression: str) -> bool:
        lastOperator = []
        for subExpr in expression:
            if subExpr == ')':
                op =  lastOperator.pop()
                if op == '!':
                    res = self.parseNegate()
                    self.stack.pop()
                    self.stack.append(res)
                elif op == '&':
                    res = self.parseAnd()
                    self.stack.pop()
                    self.stack.append(res)
                else:
                    res = self.parseOr()
                    self.stack.pop()
                    self.stack.append(res)
                #print(self.stack)
            elif subExpr == 't' or subExpr == 'f':
                self.stack.append(subExpr)
            elif subExpr == '!' or subExpr == '&' or subExpr == '|':
                lastOperator.append(subExpr)
                self.stack.append(subExpr)
        #p//rint(self.stack)
        #print(lastOperator)
        last = self.stack.pop()
        return True if last == 't' else False
