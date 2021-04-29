import sys; sys.stdin = open('input_data/2141.txt')
town = int(input())
town_list = []
population = 0
for _ in range(town):
    town_data = list(map(int, input().split()))
    town_list.append(town_data)
    population += town_data[1]
town_list.sort()
now = 0
for in_town in town_list:
    now += in_town[1]
    if now >= population/2:
        print(in_town[0])
        break