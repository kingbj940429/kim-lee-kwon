from collections import deque


def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5

    answer = 0
    cache = set()
    queue = deque()

    for c in cities:
        c = c.lower()
        if c in cache:
            queue.remove(c)
            queue.append(c)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.remove(queue.popleft())
            cache.add(c)
            queue.append(c)
            answer += 5

    return answer
