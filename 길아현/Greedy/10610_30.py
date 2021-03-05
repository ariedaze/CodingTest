N = input()

if '0' in N:
    N_list = list(N)
    if sum(list(map(int, N_list))) % 3 == 0:
        print(''.join(sorted(N_list, reverse=True)))
    else:
        print(-1)
else:
    print(-1)
