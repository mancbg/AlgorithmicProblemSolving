MIDDLE = 5


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # Numbers left
    sequence = [8, 3, 4, 9, 2, 7, 6, 1]

    # Middle element is always 5, so that's the minimum cost we always need
    res = abs(s[4] - MIDDLE)

    s = [s[0], s[1], s[2], s[5], s[8], s[7], s[6], s[3]]

    accum = float('inf')

    for i in range(4):
        accum = min(accum, get_sum(s, sequence, res), get_sum(s, [sequence[0]] + sequence[1:][::-1], res))
        sequence = sequence[2:] + sequence[:2]
        print()

    return accum


def get_sum(num, seq, res):
    for i in range(len(num)):
        res += abs(num[i] - seq[i])
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    square = [4, 5, 8, 2, 4, 1, 1, 9, 7]

    # for _ in range(3):
    #     square.extend(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(square)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
