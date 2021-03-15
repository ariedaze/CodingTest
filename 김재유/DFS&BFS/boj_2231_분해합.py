import sys; sys.stdin = open('input_data/2231.txt')

result = 0

N_str = input()
N_int = int(N_str)
for number in range(max(N_int-len(N_str)*9, 0), N_int + 1):
    N_list = list(map(int, ' '.join(str(number)).split()))
    if number+sum(N_list) == N_int:
        result = number
        break
print(result)


