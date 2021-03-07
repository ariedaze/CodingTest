import sys; sys.stdin = open('input_data/1700.txt')

tap_size, N = map(int, input().split())
electrics = list(map(int, input().split()))
tap = electrics[:tap_size]
electrics = electrics[tap_size:]
tap_distance=[10000] * tap_size
for i in range(tap_size):
    try:
        tap_distance[i] = electrics.index(tap[i])
    except:
        pass

result = 0
for _ in range(len(electrics)):
    electric = electrics.pop(0)
    if electric in tap:
        pass
    else:
        result += 1
        kill = tap_distance.index(max(tap_distance))
        tap[kill] = electric
        for i in range(tap_size):
            try:
                tap_distance[i] = electrics.index(tap[i])
            except:
                tap_distance[i] = 10000
print(result)




