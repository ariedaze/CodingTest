import sys; sys.stdin = open('input_data/2664.txt')

def findParent(x):
    global count
    count += 1
    visit[x] = 1
    if x == my_x:
        result.append(count)
    else:
        for i in family[x]:
            if not visit[i]:
                findParent(i)
                count -= 1
                visit[i] = 0

people = int(input())
my_x, my_y = map(int, input().split())
family = [[0] for i in range(people+1)]
line_num = int(input())
for _ in range(line_num):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child][0] = parent
visit = [0] * (people+1)
count = -1
result = []
findParent(my_y)
if result:
    print(result[0])
else:
    print(-1)