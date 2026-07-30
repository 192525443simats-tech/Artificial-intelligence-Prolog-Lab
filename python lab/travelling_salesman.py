from itertools import permutations

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

cities = [1,2,3]

min_path = float('inf')

for perm in permutations(cities):
    cost = 0
    k = 0

    for j in perm:
        cost += graph[k][j]
        k = j

    cost += graph[k][0]

    min_path = min(min_path, cost)

print("Minimum Cost =", min_path)