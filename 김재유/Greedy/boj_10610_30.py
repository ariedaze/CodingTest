num_list = list(map(int, ' '.join(input()).split()))

if 0 in num_list and not sum(num_list)%3:
    num_list.sort(reverse=True)
    print(''.join(list(map(str, num_list))))
else:
    print(-1)