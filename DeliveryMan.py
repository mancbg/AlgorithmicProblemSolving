def deliveryMan(n, x, y, a, b):
    sum = 0
    differences = dict()
    for i in range(n):
        if abs(a[i] - b[i]) in differences.keys():
            differences[abs(a[i] - b[i])].append(i)
        else:
            differences[abs(a[i] - b[i])] = [i]
    for d in sorted(differences.keys(), reverse=True):
        for i in differences[d]:
            if a[i] > b[i]:
                if x > 0:
                    sum += a[i]
                    x -= 1
                else:
                    sum += b[i]
                    y -= 1
            else:
                if y > 0:
                    sum += b[i]
                    y -= 1
                else:
                    sum += a[i]
                    x -= 1
    return sum


if __name__ == '__main__':
    N, X, Y = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    res = deliveryMan(N, X, Y, A, B)
    print(res)
