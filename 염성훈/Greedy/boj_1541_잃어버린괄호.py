import sys
sys.stdin = open("input.txt","r")

input = sys.stdin.readline()

arr = []

N = len(input)
number = ""
for item in input:
    if item != '-' and item != '+':
        number += item
    else :
        arr.append(number)
        number = ""
        arr.append(item)

print(arr)