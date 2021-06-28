def solution(numbers):
    answer = []

    for number in numbers:
        #바이너리로 변환할 경우 0x이런식으로 나오기 때문에 아래와 같은 처리를 해줘야한다.
        bin_number = list('0' + bin(number)[2:])
        #오른쪽에서부터 0을 찾고 인덱스에 1을 대입하면 다음 수를 찾을 수가 있다.
        #rfind() = 오른쪽에서 탐색해서 가장 먼저의 인덱스를 반환한다.
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        #홀수의 경우 다음 인덱스의 값을 0으로 바꿔주면 답이 나오게 된다.
        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        #int로 2진수의 값을 10진수로 변환할 수 있다.
        answer.append(int(''.join(bin_number),2))

    return answer

numbers = [2, 7]
solution(numbers)