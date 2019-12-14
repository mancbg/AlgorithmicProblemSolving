def cultural_programme(entry_records, exit_records):
    max_audience = 0
    current_audience = 0

    total_records = sorted(entry_records.union(exit_records))

    for current_time in total_records:
        if current_time in entry_records:
            current_audience += 1
        else:
            current_audience -= 1
        max_audience = max(max_audience, current_audience)

    return max_audience


def main():
    entries, exits = set(), set()
    for _ in range(int(input())):
        p_entry, p_exit = map(int, input().split())
        entries.add(p_entry)
        exits.add(p_exit)
    print(cultural_programme(entries, exits))


if __name__ == '__main__':
    main()
