import sys; sys.stdin=open('input_data/12886.txt')
from collections import deque

def ANABADA(X, Y):
    Y -= X
    X += 2
    if Y <= 0:
        return [-1, -1]
    return [X, Y]

first = list(map(int, input().split()))
visit = [[[0]*501 for _ in range(501)] for _ in range(501)]
Q = deque()
Q.append(first)
if first[0] == first[1] == first[2]:
    print(1)
elif sum(first)%3 or sum(first)%2 or 0 in first:
    print(0)
print(visit)
# else:
#     while Q:
#         A, B, C = Q.popleft()
#         visit[A][B][C] = 1
#         if A != B:
#             new = ANABADA(A, B) + [C]
#             if new[0] == new[1] == new[2]:
#                 print(1)
#                 break
#             new.sort()
#             if new[0] != -1 and not visit[new[0]][new[1]][new[2]]:
#                 Q.append(new)
#                 visit[new[0]][new[1]][new[2]] = 1
#         if B != C:
#             new = ANABADA(B, C) + [A]
#             if new[0] == new[1] == new[2]:
#                 print(1)
#                 break
#             new.sort()
#             if new[0] != -1 and not visit[new[0]][new[1]][new[2]]:
#                 Q.append(new)
#                 visit[new[0]][new[1]][new[2]] = 1
#         if A != C:
#             new = ANABADA(A, C) + [B]
#             if new[0] == new[1] == new[2]:
#                 print(1)
#                 break
#             new.sort()
#             if new[0] != -1 and not visit[new[0]][new[1]][new[2]]:
#                 Q.append(new)
#                 visit[new[0]][new[1]][new[2]] = 1
#     else:
#         print(0)