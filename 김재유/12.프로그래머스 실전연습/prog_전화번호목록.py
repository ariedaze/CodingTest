def solution(phone_book):
    length = len(phone_book)
    for i in range(length):
        for j in range(i+1, length):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
            else:
                if phone_book[j] == phone_book[i][:len(phone_book[j])]:
                    return False
    return True