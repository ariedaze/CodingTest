from itertools import combinations

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

closet = {}
count = []
for cloth in clothes:
    if cloth[1] not in closet.keys():
        closet[cloth[1]] = 1
    else:
        closet[cloth[1]] += 1
count = closet.values()

result = len(clothes)
for i in range(2, len(count) + 1):
    num_list = list(map(list, combinations(count,i)))
    for nums in num_list:
        now = 1
        for num in nums:
            now *= num
        result+= now
print(result)

