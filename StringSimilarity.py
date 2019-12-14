def string_similarity(s):
    return z_algorithm(s)


def z_algorithm(s):
    z = [0] * len(s)
    z[0] = len(s)
    l, r = 0, 0
    res = z[0]
    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            l, r = z_compare(s, l, r)
            z[i] = r - l
        else:
            k = i - l
            if z[k] < r - i:
                z[i] = z[k]
            else:
                l = i
                r = z_compare(s, l, r)[1]
                z[i] = r - l
        res += z[i]
    return res



def z_compare(s, l, r):
    while r < len(s) and s[r - l] == s[r]:
        r += 1
    return l, r


def main():
    s = 'ababaa'
    print(string_similarity(s))


if __name__ == '__main__':
    main()
