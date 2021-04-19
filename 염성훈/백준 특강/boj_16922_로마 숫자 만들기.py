import sys
sys.stdin = open("input.txt","r")
from itertools import combinations_with_replacement
# 처음에는 dict로 구성해줘야하나 생각했는데 굳이 그럴필요없이 nums를 리스트로 담아주면 됨.
# 일일이 String으로 뽑을 필요가 없어짐
nums = [1, 5, 10, 50]
N = int(input())
result = []
# 중복된 조합값을 튜플로 뽑는다. 중복된 값이 여러번 뽑혀도 되기 때문에 사용한다.
for item in combinations_with_replacement(range(4),N):
    print(item)
    num_sum = 0
    # 뽑힌 튜플 값을 num_sum에 더해서 값을 뽑고 더한 값이 서로 다른 수의 개수를 출력해야하기 때문에 if문 처리를 해준다.
    for i in item:
        num_sum += nums[i]
    if num_sum not in result:
        result.append(num_sum)

print(len(result))

