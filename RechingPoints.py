class Solution:
    def reachingPoints(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        while x2 >= x1 and y2 >= y1:
            if x2 == y2:
                break
            elif x2 > y2:
                if y2 > y1:
                    x2 %= y2
                else:
                    return (x2 - x1) % y2 == 0
            else:
                if x2 > x1:
                    y2 %= x2
                else:
                    return (y2 - y1) % x2 == 0
        return x1 == x2 and y1 == y2


if __name__ == '__main__':
    s1 = int(input())
    s2 = int(input())
    t1 = int(input())
    t2 = int(input())

    print(Solution().reachingPoints(s1, s2, t1, t2))
