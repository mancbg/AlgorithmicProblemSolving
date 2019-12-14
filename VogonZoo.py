def vogon_zoo(dragon_bloods, threshold):
    max_dragons = 0

    dragon_bloods = sorted(dragon_bloods)
    current = dragon_bloods[0] - threshold

    for blood_type in dragon_bloods:
        if blood_type - current >= threshold:
            max_dragons += 1
            current = blood_type

    return max_dragons


def main():
    num_dragons, threshold = map(int, input().split())
    dragons_blood_type = list(map(int, input().split()))

    assert num_dragons == len(dragons_blood_type)

    print(vogon_zoo(dragons_blood_type, threshold))


if __name__ == '__main__':
    main()
