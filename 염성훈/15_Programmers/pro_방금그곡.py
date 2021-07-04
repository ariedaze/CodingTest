def change(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    m = change(m)
    flag = False
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = 60 * (end_h - start_h) + (end_m - start_m)
        melody = change(melody)
        melody_played = (melody * time)[:time]
        if m in melody_played:
            answer.append((title, time))
            flag = True

    answer.sort(key=lambda x:x[1], reverse=True)

    if flag == False:
        return '(None)'

    return answer[0][0]

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))