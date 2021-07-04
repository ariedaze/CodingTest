def solution(files):
    answer = []
    #문자열을 저장하는 원본
    str = []
    for s in files:
        head = ''
        for char in s:
            if char.isdigit():
                break
            head += char

        number = ''
        for char in s[len(head):]:
            if not char.isdigit():
                break
            number += char

        str.append([head.lower(), int(number), s])

    #정렬의 두가지 조건을 줄떄는 아래와 같이 준다.
    str.sort(key=lambda x:(x[0], x[1]))

    for i in str:
        answer.append(i[2])

    return answer

files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)