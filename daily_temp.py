from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = CustomDeque()
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack.peek()]:
                index = stack.pop()
                answer[index] = i -index 
            stack.append(i)
        return answer
class CustomDeque(deque):
    def peek(self):
        return self[-1] if self else None  