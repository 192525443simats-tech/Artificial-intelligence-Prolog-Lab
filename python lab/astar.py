from queue import PriorityQueue

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',1)],
    'C':[('F',5)],
    'D':[],
    'E':[('F',2)],
    'F':[]
}

heuristic = {
    'A':6,
    'B':4,
    'C':4,
    'D':2,
    'E':2,
    'F':0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))

    cost = {start:0}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            print("Goal Reached:", goal)
            return

        for neighbour, weight in graph[current]:
            new_cost = cost[current] + weight

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                priority = new_cost + heuristic[neighbour]
                pq.put((priority, neighbour))

astar('A', 'F')