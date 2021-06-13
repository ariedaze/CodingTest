import sys; sys.stdin = open('input_data/9205.txt')

def get_distance(place_a, place_b):
    distance = abs(place_a[0]-place_b[0]) + abs(place_a[1]-place_b[1])
    if distance <= 1000:
        return True
    else:
        return False

def DFS(place):
    global result
    if result == "happy":
        return
    if get_distance(place[1:], destination):
        result = "happy"
        return

    for store in stores:
        if not visit[store[0]] and get_distance(place[1:], store[1:]):
            visit[store[0]] = 1
            DFS(store)
            visit[store[0]] = 0

for t in range(int(sys.stdin.readline())):
    num_store = int(input())
    home = list(map(int, sys.stdin.readline().split()))
    stores = [[i] + list(map(int, sys.stdin.readline().split())) for i in range(num_store)]
    destination = list(map(int, sys.stdin.readline().split()))
    result = "sad"

    for store in stores:
        visit = [0] * num_store
        if result == "sad" and get_distance(home, store[1:]):
            visit[store[0]] = 1
            DFS(store)
            visit[store[0]] = 0
        else:
            break
    print(result)