# import sys
# sys.stdin = open('input/예상 대진표.txt', 'r')

def solution(n,a,b): 
	answer = 0
	while a != b: 
		answer += 1
		a, b = (a+1)//2, (b+1)//2
        
	return answer