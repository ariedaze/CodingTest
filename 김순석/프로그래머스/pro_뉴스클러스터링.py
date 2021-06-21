def solution(str1, str2):
    answer = 0
    A = []
    B = []

    tmp1 = str1.lower()
    tmp2 = str2.lower()

    for i in range(len(tmp1) - 1):
        if tmp1[i].isalpha() and tmp1[i+1].isalpha():
            A.append(tmp1[i:i + 2])

    for j in range(len(tmp2) - 1):
        if tmp2[j].isalpha() and tmp2[j + 1].isalpha():
            B.append(tmp2[j:j + 2])
    # print(A, B)
    comm, union = multiset(A, B)
    if len(union) == 0:
        answer = 1 * 65536
    else:
        answer = len(comm) * 65536 // len(union)
    return answer


def multiset(A, B):
    a1 = A.copy()
    a2 = A.copy()
    comm = []

    for i in B:
        if i not in a1:
            a2.append(i)
        else:
            a1.remove(i)
    for j in B:
        if j in A:
            A.remove(j)
            comm.append(j)
    return comm, a2