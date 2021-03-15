import sys
sys.stdin = open("input.txt","r")

from itertools import permutations

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(permutations(n,3)) #모든 경우의수를 받기위해 9까지의 숫자중 3개를 뽑아 순열로 만들어준다.

length = len(num)

N = int(input())

for _ in range(N):
    numbers, strike, ball = map(int,input().split())
    div_number = list(str(numbers))
    remove_cnt = 0 #remove되는 만큼 배열의 길이가 감소하기 떄문에 정해줘야한다.

    for i in range(len(num)):
        strike_cnt = ball_cnt = 0
        i -= remove_cnt #그만큼 뺴줘야 다음 범위 오류가 발생하지 않는다.

        for j in range(3):
            if int(div_number[j]) in num[i]:
                if j == num[i].index(int(div_number[j])):
                    strike_cnt += 1
                else :
                    ball_cnt += 1
        if strike_cnt != strike or ball_cnt != ball: #스트라이크와 볼카운트가 다르면 배열에서 빼준다.
            num.remove(num[i])
            remove_cnt += 1

print(len(num))
