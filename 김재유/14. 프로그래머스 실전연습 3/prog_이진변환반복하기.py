def solution(s):
    answer = []
    count = 0
    zero = 0
    while s != "1":
        count += 1
        zero += s.count("0")
        s = str(bin(s.count("1")))[2:]
    return [count, zero]