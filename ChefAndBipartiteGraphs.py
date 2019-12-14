def chef_and_bipartite_graphs(n, m, d, D):
    if m < d * n or m > D * n:
        return -1

    min_edges, extra_edges = divmod(m, n)

    for v in range(n):
        # Minimum edges for each vertex
        for deg in range(min_edges):
            print(v + 1, ((v + deg) % n) + 1)

    for v in range(extra_edges):
        print(v + 1, ((v + min_edges) % n) + 1)


def main():
    T = int(input())

    for _ in range(T):
        n, m, d, D = map(int, input().strip().split())

        if chef_and_bipartite_graphs(n, m, d, D):
            print(-1)


if __name__ == '__main__':
    main()
