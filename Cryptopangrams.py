def decrypt(n, products):
    gcd_index = None
    first_num, second_num = None, None

    # Sequence of prime numbers representing letters
    sequence = [None] * (len(products) + 1)

    for i in range(0, len(products) - 1):
        if products[i] != products[i + 1]:
            gcd_index = i + 1
            first_num = products[i]
            second_num = products[i + 1]
            break
    gcd = find_gcd(first_num, second_num)
    sequence[gcd_index] = gcd

    for index in range(gcd_index - 1, -1, -1):
        gcd = products[index] // gcd
        sequence[index] = gcd

    gcd = sequence[gcd_index]
    for index in range(gcd_index, len(products)):
        gcd = products[index] // gcd
        sequence[index + 1] = gcd

    prime_numbers = sorted(set(sequence))
    primes_to_letters = dict()

    for index in range(len(prime_numbers)):
        primes_to_letters[prime_numbers[index]] = chr(97 + index)

    result = ""
    for prime in sequence:
        result += primes_to_letters[prime]

    return result


def find_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2

    return num2


def main():
    test_cases = int(input())
    case_num = 1

    for _ in range(test_cases):
        n, l = map(int, input().split())
        products = list(map(int, input().split()))

        assert l == len(products)
        decrypted_message = decrypt(n, products)

        print("Case #%s: %s" % (case_num, decrypted_message))
        case_num += 1


if __name__ == '__main__':
    main()
