import sys


def main():
    count = int(input())
    numbers = list()
    for i in range(2, count + 2):
        numbers.append(int(input()))
    case = 1
    for num in numbers:
        issue_checks(num, case)
        case += 1



def issue_checks(num, case_num):
    digits = list(int(d) for d in str(num))
    result = ""
    result_left = ""
    flag = False
    for digit in digits:
        if digit != 4:
            result += str(digit)
            if flag:
                result_left += str(0)
        else:
            result += str(2)
            result_left += str(2)
            flag = True
    print("Case #%s: %s %s" % (case_num, result, result_left))


if __name__ == '__main__':
    main()
