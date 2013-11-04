import sys
from collections import defaultdict


def main():
    num_cases = int(sys.stdin.readline())

    for j in range(num_cases):
        case_num = j + 1
        line = sys.stdin.readline()
        chars = defaultdict(int)

        for char in line:
            chars[char] = chars[char] + 1

        count = chars["C"] / 2

        if chars["H"] < count:
            count = chars["H"]
        if chars["A"] < count:
            count = chars["A"]
        if chars["K"] < count:
            count = chars["K"]
        if chars["E"] < count:
            count = chars["E"]
        if chars["R"] < count:
            count = chars["R"]
        if chars["U"] < count:
            count = chars["U"]
        if chars["P"] < count:
            count = chars["P"]

        print "Case #" + str(case_num) + ": " + str(count)

if __name__ == '__main__':
    main()
