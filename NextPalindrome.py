"""
Author: Manasi Gund
Source: CodeChef
Link: https://www.codechef.com/problems/PALIN
"""


def get_middle(number):
    mid = int(len(number) // 2)
    if len(number) % 2 == 0:
        return mid - 1, mid
    else:
        return mid, mid


def next_palindrome(number):
    if number == '9' * len(number):
        return '1' + ('0' * int(len(number) - 1)) + '1'
    number = [ch for ch in number]
    i, j = get_middle(number)
    while i >= 0 and j < len(number) and number[i] == number[j]:
        i -= 1
        j += 1
    switch = False
    if i < 0 or number[i] < number[j]:
        switch = True
    if switch:
        i, j = get_middle(number)
        carry = False
        while number[i] == '9':
            number[i] = '0'
            number[j] = number[i]
            carry = True
            i -= 1
            j += 1
        if i >= 0 or carry:
            number[i] = str(int(number[i]) + 1)
    while i >= 0:
        number[j] = number[i]
        i -= 1
        j += 1
    return ''.join(number)


def main():
    for _ in range(int(input())):
        print(next_palindrome(input()))


if __name__ == '__main__':
    main()
