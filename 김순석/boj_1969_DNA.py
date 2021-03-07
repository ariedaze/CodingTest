# N, M 크기 보니까 이중 for문 써도 되겠다 싶었음.
import sys
from collections import Counter

In = sys.stdin.readline

N, M = map(int, In().split())
lst = [In().rstrip() for i in range(N)]

ans = []
cnt = 0

for i in range(M):
    # 1~M번째 자리의 문자를 넣어서 카운트할 리스트
    cnt_lst = []
    for j in range(N):
        cnt_lst.append(lst[j][i])

    counter = Counter(cnt_lst)
    max_cnt = -1

    # dist가 같을 때 사전 순으로 정렬
    sort_counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    for letter, val in sort_counter:
        # 위에서 사전 순으로 정렬해놔서 등호 없이 구현
        if val > max_cnt:
            max_cnt = val
            max_letter = letter

    ans.append(max_letter)
    cnt += N - max_cnt


for i in ans:
    print(i, end='')
print()
print(cnt)
