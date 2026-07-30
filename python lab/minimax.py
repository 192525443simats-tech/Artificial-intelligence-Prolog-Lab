scores = {'X': 1, 'O': -1, 'Draw': 0}

def minimax(depth, isMax):
    if depth == 0:
        return 0

    if isMax:
        best = -1000
        for _ in range(2):
            best = max(best, minimax(depth - 1, False))
        return best
    else:
        best = 1000
        for _ in range(2):
            best = min(best, minimax(depth - 1, True))
        return best

print("Best Score:", minimax(3, True))