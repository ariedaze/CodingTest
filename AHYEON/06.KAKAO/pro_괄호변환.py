def check(p):
    if p == '':  # 1
        return ''
    u, v = split(p)  # 2 두 균형잡힌 괄호 문자열로 분리, i
    if right(u):  # 3  u가 올바른 괄호 문자열이라면 v에 대해 1단계부터 수행
        return u + check(v)  # 3-1
    else:  # 4
        return '(' + check(v) + ')' + reverse(u[1:-1])


def split(p):
    for i in range(len(p)):
        u = p[:i+1]
        o = u.count('(')
        c = u.count(')')
        if o == c and o + c < len(p):
            return u, p[i+1:]
    return p, ""


def right(p):
    q = []
    for i in p:
        if i == '(':
            q.append(i)
        else:
            if q:
                q.pop()
            else:
                return False
    if q: return False
    return True


def reverse(p):
    r = ''

    for i in p:
        if i == '(':
            r += ')'
        else:
            r += '('
    return r


def solution(p):
    return check(p)

