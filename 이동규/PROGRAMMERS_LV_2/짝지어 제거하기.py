# import sys
# sys.stdin = open('input/짝지어 제거하기.txt', 'r')

from collections import deque

def solution(s):
    
    ORIGIN = deque(list(s))
    stack = deque()
    stack.append(ORIGIN.popleft())
    top = stack[0]
    
    while ORIGIN:
        selected = ORIGIN.popleft()
        if stack and top == selected:
            stack.pop()
            top = stack[-1] if stack else None
        else:
            top = selected
            stack.append(top)
    
    if stack:
        return 0
    else:
        return 1