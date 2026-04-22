def alpha_beta(depth, node, is_max, values, alpha, beta):
    # Leaf node
    if depth == 3:
        return values[node]

    if is_max:
        best = -999
        for i in range(2):  # 2 children per node
            val = alpha_beta(depth+1, node*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"  Pruned at depth {depth+1}, node {node*2+i}")
                break
        return best
    else:
        best = 999
        for i in range(2):
            val = alpha_beta(depth+1, node*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"  Pruned at depth {depth+1}, node {node*2+i}")
                break
        return best

# Leaf values (8 leaves for depth-3 tree)
values = [3, 5, 2, 9, 1, 7, 4, 6]

result = alpha_beta(0, 0, True, values, float('-inf'), float('inf'))
print("Optimal value:", result)