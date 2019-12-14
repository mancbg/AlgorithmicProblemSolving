"""
author: Manasi Gund
Source: CodeJam
Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000003005a
"""
WAFFLE_THINGS = {'.': 0, "@": 1}


def waffle_choppers(grid, total_chips, R, C, H, V):
    """
    Find if it's possible to make exactly H row cuts and V column cuts
    such as every piece will have the same number of chocolate chip.
    Here chocolate chip is denoted by @ in the grid
    :param grid: Grid of . and @ indicating . = nothing and @ = chocolate chip
    :param num_chips: number of '@', chocolate chip
    :param R: Rows of grid
    :param C: Columns of grid
    :param H: # of Horizontal cuts needed
    :param V: # of Vertical cuts
    :return: Boolean True if possible to have same number of chips, False otherwise
    """
    # Minimum chocolate chips
    min_chips = (H + 1) * (V + 1)

    # If not possible to divide the total chips into equal
    if total_chips % min_chips != 0:
        return False

    # If no chocolate chips, it is always possible to have equal chips = 0
    if total_chips == 0:
        return True

    # Possible to divide with horizontal cuts
    if total_chips % (H + 1) != 0:
        return False

    # Each horizontal slice should have these many chips
    h_chips = total_chips // (H + 1)

    # Slices cut so far
    h_slices = list()

    # Chips before the last horizontal cut
    previous_slice = 0

    # Horizontal cuts after each row -> gives the sum of total chocolate chips
    # before that cut
    row_sum = [0] * (R + 1)
    for row in range(1, R + 1):
        row_sum[row] = row_sum[row - 1] + grid[row - 1].count('@')
        chip_count = row_sum[row] - row_sum[previous_slice]
        if chip_count < h_chips:
            continue
        elif chip_count == h_chips:
            h_slices.append((previous_slice, row - 1))
            previous_slice = row
        else:
            return False

    # Possible to divide with horizontal cuts
    if total_chips % (V + 1) != 0:
        return False

    # Each horizontal slice should have these many chips
    v_chips = total_chips // (V + 1)

    # Slices cut so far
    v_slices = list()

    # Chips before the last horizontal cut
    previous_slice = 0

    # Vertical cuts after each column -> gives the sum of total chocolate chips
    # before that cut
    col_sum = [0] * (C + 1)
    for col in range(1, C + 1):
        col_sum[col] = col_sum[col - 1] + [x[col - 1] for x in grid].count('@')
        chip_count = col_sum[col] - col_sum[previous_slice]
        if chip_count < v_chips:
            continue
        elif chip_count == v_chips:
            v_slices.append((previous_slice, col - 1))
            previous_slice = col
        else:
            return False

    each = total_chips // min_chips

    # Even if we check horizontal and vertical cuts
    # We still need to check if all those cuts put together
    # give us equal number of chips in each piece
    for h in h_slices:
        for v in v_slices:
            if not count_chips(grid, h, v, each):
                return False

    return True


def count_chips(grid, h_interval, v_interval, count):
    for i in range(h_interval[0], h_interval[1] + 1):
        for j in range(v_interval[0], v_interval[1] + 1):
            count -= WAFFLE_THINGS[grid[i][j]]
    return count == 0


def main():
    T = int(input())

    for i in range(T):
        R, C, H, V = map(int, input().strip().split())
        waffle_grid = list()
        chocolate_chips = 0

        for r in range(R):
            ip = input().strip()
            chocolate_chips += ip.count('@')
            row = list(ip.strip())
            assert C == len(row)
            waffle_grid.append(row)

        doable = "POSSIBLE" if waffle_choppers(waffle_grid, chocolate_chips, R, C, H, V) else "IMPOSSIBLE"

        print("Case #" + str(i + 1) + ": " + doable)


if __name__ == '__main__':
    main()
