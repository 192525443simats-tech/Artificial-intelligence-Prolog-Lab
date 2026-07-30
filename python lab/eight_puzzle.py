from collections import deque

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        visited.add(state_to_tuple(state))

        x, y = find_zero(state)

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if state_to_tuple(new_state) not in visited:
                    queue.append((new_state, path+[state]))

solution = bfs(start)

for step in solution:
    for row in step:
        print(row)
    print()