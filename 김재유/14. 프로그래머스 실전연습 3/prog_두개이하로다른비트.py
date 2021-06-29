def solution(numbers):
    answer = []
    for number in numbers:
        if number%2:
            binnum = list(' '.join(str(bin(number))[2:]).split())
            if "0" not in binnum:
                binnum[0] = "0"
                binnum.insert(0, "1")
            else:
                for i in range(len(binnum)-1, -1, -1):
                    if binnum[i] == "0":
                        binnum[i] = "1"
                        for j in range(i+1,len(binnum)):
                            if binnum[j] == "1":
                                binnum[j] = "0"
                                break
                        break
            answer.append(int(''.join(binnum),2))
        else:
            answer.append(number+1)

    return answer