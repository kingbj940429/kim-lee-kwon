from collections import deque


def keep_distance(place, positions, directions, *start):
    visited = {start}
    queue = deque([start])
    for _ in range(2):
        for __ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in positions and place[nx][ny] != 'X' and (nx, ny) not in visited:
                    if place[nx][ny] == 'P':
                        return False
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return True


def solution(places):
    answer = []
    positions = {(i, j) for i in range(5) for j in range(5)}
    directions = (-1, 0), (0, 1), (1, 0), (0, -1)
    for place in places:
        for i, j in positions:
            if place[i][j] == 'P' and not keep_distance(place, positions, directions, i, j):
                answer.append(0)
                break
        else:
            answer.append(1)
    return answer
