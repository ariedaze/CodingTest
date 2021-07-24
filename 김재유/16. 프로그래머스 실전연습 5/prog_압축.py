def solution(msg):
    words = {
        "A":1, "B":2, "C": 3, "D": 4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
        "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
        "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26
    }
    idx = 27
    max_length = 1
    result = []
    now = 0
    while now < len(msg):
        for length in range(max_length, 0, -1):
            if now + length <= len(msg):
                word = msg[now:now+length]
                if word in words.keys():
                    result.append(words[word])
                    if now + length +1 <= len(msg):
                        next_word = msg[now:now+length+1]
                        words[next_word] = len(words) +1
                        max_length = max(max_length, len(next_word))
                    now += length
    print(words)
    return result

msg = "TOBEORNOTTOBEORTOBEORNOT"
solution(msg)