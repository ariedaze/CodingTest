import sys
sys.stdin = open('input/boj_12904_A와 B.txt', 'r')

ORIGIN = list(input())
COMP = list(input())

# HEADER = COMP[0:len(ORIGIN)]
# OFFSET = COMP[len(ORIGIN):]
#
# temp = OFFSET[0]
# for i in OFFSET[1:]:
#     if temp == i:
#         temp = 'A'
#     else:
#         temp = 'B'
#
# if (HEADER == ORIGIN and temp == 'B') or (HEADER != ORIGIN and temp == 'A'):
#     print(0)
# else:
#     print(1)

while len(ORIGIN) != len(COMP):
    if COMP[-1] == 'A':
        COMP.pop()
    else:
        COMP.pop()
        COMP = COMP[::-1]

print(1 if ORIGIN == COMP else 0)