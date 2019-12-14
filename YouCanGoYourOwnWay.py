def main():
    test_cases = int(input())
    case_num = 1
    for tc in range(test_cases):
        dim = int(input())
        l_path_str = input()
        path = ""
        for i in l_path_str:
            if i == "S":
                path += "E"
            else:
                path += "S"
        if path != "":
            print("Case #%s: %s" % (case_num, path))
        case_num += 1


if __name__ == '__main__':
    main()
