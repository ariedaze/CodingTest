import sys
sys.stdin = open("input.txt","r")
from itertools import  combinations

while True:
    numList = list((map(int,input().split())))
    k = numList[0]
    if k == 0:
        break
    newList = numList[1:]
    result = list(combinations(newList,6))

    for items in result:
        for item in items:
            print(item, end=" ")
        print()
    print()

