import sys


def main():

    tokens = []

    for line in sys.stdin.readlines():
        for token in line.split():
            tokens.append(token)

    num_cases = int(tokens.pop(0))

    for case_num in xrange(1, num_cases + 1):
        print "Case #" + str(case_num) + ": " + str(recover())

    # print "Ready!"


# sequence_length (int) the number of sequential integers in the sequence
# log (string) log of 1's and 2's. 1 = <, 2 = >
#
# return (int) the question specific hash of the resulting sequence
def recover(sequence_length, log):
    seq, _ = reverse_sort(range(1, sequence_length + 1), [c for c in log])
    print "Reversed to seq: " + str(seq)
    return checksum(seq)


def checksum(seq):
    result = 1
    for i in xrange(len(seq)):
        result = (31 * result + seq[i]) % 1000003
    return result


# seq (list(int))
# log (list(string))
def reverse_sort(seq, log):

    print "Passed seq:" + str(seq) + " and log:" + str(log) + " to reverse_sort"

    if (len(seq) == 1):
        return seq, log

    (left, right, log) = reverse_merge(seq, log)
    (right, log) = reverse_sort(right, log)
    (left, log) = reverse_sort(left, log)

    return (left + right), log


# seq (list(int)) sequence of integers to be reverse merged
# log (list(string)) the remaining portion of the log
#
# return ((list(int), list(int), string))
def reverse_merge(seq, log):

    print "Passed seq:" + str(seq) + " and log:" + str(log) + " to reverse_merge"

    # deal with the final segment that was appended without any logging
    mid = len(seq) / 2
    remaining_1 = mid
    remaining_2 = len(seq) - mid

    # work out how many need to be added before working backwards on the log
    i = len(log) - 1
    while remaining_1 > 0 and remaining_2 > 0:
        if log[i] == '1':
            remaining_1 = remaining_1 - 1
        elif log[i] == "2":
            remaining_2 = remaining_2 - 1
        else:
            print "Someone done fucked up."
        i = i - 1

    result_1 = []
    result_2 = []

    print "Remaining 1: " + str(remaining_1)
    print "Remaining 2: " + str(remaining_2)

    # only 1 of these loops runs each time
    while remaining_1 > 0:
        result_1.insert(0, seq.pop())
        remaining_1 = remaining_1 - 1

    while remaining_2 > 0:
        result_2.insert(0, seq.pop())
        remaining_2 = remaining_2 - 1

    # put the rest back in using the log
    while len(seq) > 0:
        if log.pop() == "1":
            result_1.insert(0, seq.pop())
            remaining_1 = remaining_1 - 1
        else:
            result_2.insert(0, seq.pop())
            remaining_2 = remaining_2 - 1

    return (result_1, result_2, log)


if __name__ == "__main__":
    main()
