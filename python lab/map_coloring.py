states = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
assignment = {}

def is_safe(state, color):
    for neighbor in neighbors[state]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(index):
    if index == len(states):
        return True

    state = states[index]

    for color in colors:
        if is_safe(state, color):
            assignment[state] = color

            if solve(index + 1):
                return True

            assignment.pop(state)

    return False

solve(0)

print("Map Coloring Solution:")
for state in assignment:
    print(state, "->", assignment[state])