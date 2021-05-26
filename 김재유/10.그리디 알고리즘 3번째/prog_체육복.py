def solution(n, lost, reserve):
    for poor in lost:
        if poor in reserve:
            lost.remove(poor)
            reserve.remove(poor)
    for poor in lost:
        if poor in reserve:
            lost.remove(poor)
            reserve.remove(poor)
    for poor in lost:
        if poor in reserve:
            lost.remove(poor)
            reserve.remove(poor)
    if len(reserve) > 0:
        for kind in reserve:
            if kind - 1 in lost:
                lost.remove(kind-1)
                continue
            elif kind + 1 in lost:
                lost.remove(kind+1)
    return  n - len(lost)