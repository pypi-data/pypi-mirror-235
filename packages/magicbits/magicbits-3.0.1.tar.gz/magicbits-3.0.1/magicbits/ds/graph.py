def graph_input() -> list:
    v = int(input("Enter the number of nodes: "))
    e = int(input("Enter the number of edges: "))

    adj_matrix = [[0] * v for _ in range(v)]

    for _ in range(e):
        u, v, w = map(int, input(f"Enter edges {_ + 1} weights: ").split())
        adj_matrix[v][u] = adj_matrix[u][v] = w

    for row in adj_matrix:
        print(row)

    return adj_matrix

if __name__ == '__main__':
    graph=graph_input()
    print(graph)
