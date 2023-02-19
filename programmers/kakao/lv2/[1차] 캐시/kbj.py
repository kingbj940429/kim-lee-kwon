# 문제이해, 접근방식, 코드설계, 코드구현
# 도시 갯수가 10^5 이므로 n^2 일 시 시간초과 가능성 있음
# Queue 문제

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = deque()

    for city in cities:
        city = city.lower()

        if city not in cache:
            answer += 5

            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
        elif city in cache:
            answer += 1

            cache.remove(city)
            cache.append(city)

    return answer

if __name__=="__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

    print(solution(cacheSize, cities))