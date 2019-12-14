# cook your dish here
def domino_solitaire(n, tiles):
    score_previous = 0
    score_previous_2 = abs(tiles[0][0] - tiles[1][0])

    for i in range(1, len(tiles[0])):
        h_current = abs(tiles[0][i] - tiles[0][i - 1]) + \
                    abs(tiles[1][i] - tiles[1][i - 1]) + \
                    score_previous
        v_current = abs(tiles[0][i] - tiles[1][i]) + score_previous_2
        score_previous = score_previous_2
        score_previous_2 = max(h_current, v_current)

    return score_previous_2


def main():
    n = int(input())
    tiles = list()
    for i in range(2):
        tiles.append(list(map(int, input().split())))

    assert n == len(tiles[0]) and n == len(tiles[1])
    print(domino_solitaire(n, tiles))


if __name__ == '__main__':
    main()
