import sys
import math


def main():
    num_cases = int(sys.stdin.readline())

    for j in range(num_cases):
        case_num = j + 1
        line = sys.stdin.readline()
        unpacked = line.split()
        width = int(unpacked.pop(0))
        height = int(unpacked.pop(0))
        largest_word = 0
        num_letters = len(line) - 4
        sizes = []

        for word in unpacked:
            # print len(word)
            length = len(word)
            sizes.append(length)
            if length > largest_word:
                largest_word = length

        # can't be so large that the longest word doesn't fit on one line.
        max_size = width / largest_word

        # can't be so large that we don't have room for all the characters.
        if width * height / num_letters < max_size * max_size:
            max_size = int(math.sqrt(width * height / num_letters))

        # print "Max size for Case #" + str(case_num) + " is " + str(max_size)

        if max_size != 0:
            for size in range(max_size, -1, -1):

                # print "Checking size " + str(size)

                chars_per_line = width / size
                max_lines = height / size

                # print str(chars_per_line) + " chars per line. " + str(max_lines) + " lines at most."
                # print "Word sizes " + str(sizes)

                current_line = 0
                current_char = 0
                current_word = 0

                while current_line < max_lines:
                    while current_word < len(unpacked):  # break when we would go over this line with the next word.
                        if (current_char + sizes[current_word] < chars_per_line) or (current_char == 0 and sizes[current_word] <= chars_per_line):
                            # print "Word " + str(current_word) + " on to line " + str(current_line)
                            if (current_char == 0):
                                current_char = sizes[current_word]
                            else:
                                current_char = current_char + sizes[current_word] + 1
                            current_word = current_word + 1
                        else:
                            break
                    current_line = current_line + 1
                    current_char = 0

                if current_word == len(unpacked):  # all the words fitted okay
                    # print the required output
                    print "Case #" + str(case_num) + ": " + str(size)
                    break
                elif size == 1:
                    # if it doesn't fit for one, print zero instead
                    print "Case #" + str(case_num) + ": 0"
                else:
                    continue


if __name__ == '__main__':
    main()
