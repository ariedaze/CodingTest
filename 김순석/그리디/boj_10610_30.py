N = list(map(int, input()))

N.sort(reverse=True)

if N[-1] != 0:
    print(-1)
else:
    if sum(N) % 3 != 0:
        print(-1)
    else:
        for i in N:
            print(i, end='')