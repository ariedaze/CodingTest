def solution(m, musicinfos):
    datas = []
    result = ""
    length = 0
    for musicinfo in musicinfos:
        music = musicinfo.split(",")
        time = int(music[1][3:]) - int(music[0][3:]) + (int(music[1][:2]) - int(music[0][:2]))*60
        song = music[3]
        sing=[]
        now = 0
        for i in range(time):
            if song[now+1] == "#":
                sing.append(song[now:now+2])
                now +=2
            else:
                sing.append(song[now])
                now += 1
            if now > len((song))-2:
                now -= len(song)
        m_length = len(m)-m.count("#")
        for i in range(time-m_length + 1):
            if m == ''.join(sing[i:i+m_length]):
                if time > length:
                    result = music[2]
                    length = time
                break
    if result:
        return result
    else:
        return "(None)"