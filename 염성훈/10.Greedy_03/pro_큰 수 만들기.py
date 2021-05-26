def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        # num의 값이 stack의 가장 상단의 값보다 크면, 기존의 값을 제거하고 새로운 값으로 대치한다.
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k!= 0:
        stack = stack[:-k]

    return ''.join(stack)

number = "4177252841"
k = 4

print(solution(number,k))