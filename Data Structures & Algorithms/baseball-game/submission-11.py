class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        stack.append(int(operations[0])) # due to constraints
        num1 = stack[-1]
        num2 = stack[-1]

        for i in range(1, len(operations)):
            if operations[i] == "+":
                result = stack[-1] + stack[-2]
                stack.append(result)
            elif operations[i] == "D":
                result = stack[-1] * 2
                stack.append(result)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)

