from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) == goal:
            return path + [(m, c, boat)]

        if (m, c, boat) in visited:
            continue

        visited.add((m, c, boat))

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:
            if boat == 1:
                nm, nc = m-dm, c-dc
                nb = 0
            else:
                nm, nc = m+dm, c+dc
                nb = 1

            if 0 <= nm <= 3 and 0 <= nc <= 3 and is_valid(nm, nc):
                queue.append(((nm, nc, nb), path + [(m, c, boat)]))

solution = bfs()

for step in solution:
    print(step)