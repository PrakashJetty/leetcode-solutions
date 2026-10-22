class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        n = len(pushed)
        already_pushed = set()
        pushed_index = 0
        popped_index = 0
        stack = []
        # stack.append(pushed[0])
        # already_pushed.add(pushed[0])
        while (popped_index < n):
            element = popped[popped_index]
            if stack and stack[-1] == element:
                stack.pop()
            elif element in already_pushed:
                return False
            else:
                while(pushed_index < n):
                    cur = pushed[pushed_index]
                    if cur != element:
                        already_pushed.add(cur)
                        stack.append(cur)
                        pushed_index += 1
                    else:
                        pushed_index += 1
                        break
                    
            popped_index += 1
        return len(stack) == 0
