opens = ["(", "{", "["]

def check_logic(check):
    q = []
    for char in check:
        if char in opens:
            q.append(char)
        else:
            if q:
                if char == ")":
                    if q.pop() != "(":
                        return 0
                if char == "}":
                    if q.pop() != "{":
                        return 0
                if char == "]":
                    if q.pop() != "[":
                        return 0
            else:
                return 0
    if q:
        return 0
    return 1


def solution(s):
    result = 0
    length = len(s)
    if length%2:
        return 0
    list_s = list(' '.join(s).split())
    for i in range(length):
        result += check_logic(list_s)
        list_s.append(list_s.pop(0))
    return result