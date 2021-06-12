def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        #앞의 것만 들어가야하므로 앞에 까지 잘라줘야한다.
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))