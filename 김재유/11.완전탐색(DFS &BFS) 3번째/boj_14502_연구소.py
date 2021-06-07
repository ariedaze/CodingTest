import sys; sys.stdin = open('input_data/14502.txt')

height, width = map(int, sys.stdin.readline().split())
Ground = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

for i in range(height):
    for j in range(width):
        if Ground[height][width] == 2:

