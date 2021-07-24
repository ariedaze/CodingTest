def solution(cacheSize, cities):
    cities = list(map(lambda x : x.lower(), cities))
    cache = []
    answer = 0
    if not cacheSize:
        return len(cities)*5
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
    return answer