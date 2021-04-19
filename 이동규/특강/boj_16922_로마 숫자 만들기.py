import sys
sys.stdin = open('input/boj_16922_로마 숫자 만들기.txt', 'r')

from itertools import combinations_with_replacement

N = int(input())
number_set_bag = set([sum(i) for i in list(combinations_with_replacement([1, 5, 10, 50], N))])
print(len(number_set_bag))

