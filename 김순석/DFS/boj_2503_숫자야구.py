import sys
sys.stdin = open('input/boj_2503_숫자야구.txt', 'r')
In = sys.stdin.readline

N = int(In())

target = [i for i in range(123, 988) if not '0' in str(i) and len(set(str(i))) == 3]
for _ in range(N):
    val, s, b = map(int, In().split())
    val = str(val)
    idx = 0
    for i in range(len(target)):
        s_cnt = b_cnt = 0
        # target에서 지웠을 때 index 맞춰주는거
        i -= idx
        for j in range(3):
            # print(type(val[j]))
            target[i] = str(target[i])
            if val[j] in target[i]:
                # print(val[j], target[i][j])
                if val[j] == target[i][j]:
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            target.remove(target[i])
            idx += 1

print(len(target))