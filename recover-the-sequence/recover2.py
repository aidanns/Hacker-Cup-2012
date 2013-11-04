import sys
# import cProfile
import collections
import itertools


def main():

    tokens = []

    for line in sys.stdin.readlines():
        for token in line.split():
            tokens.append(token)

    num_cases = int(tokens.pop(0))

    for case_num in xrange(1, num_cases + 1):
        print "Case #" + str(case_num) + ": " + str(recover(int(tokens.pop(0)), tokens.pop(0)))

    # print "Ready!"


# sequence_length (int) the number of sequential integers in the sequence
# log (string) log of 1's and 2's. 1 = <, 2 = >
#
# return (int) the question specific hash of the resulting sequence
def recover(sequence_length, log):
    seq, _ = mergesort(collections.deque([n for n in xrange(sequence_length)]), collections.deque([c for c in log]))
    orig = [0 for x in xrange(0, sequence_length)]

    for i in xrange(len(seq)):
        orig[seq[i]] = i + 1

    # print str(orig)

    return checksum(orig)


def mergesort(seq, log):

    if len(seq) == 1:
        return seq, log

    mid = len(seq) / 2

    left = collections.deque(itertools.islice(seq, 0, mid))
    right = collections.deque(itertools.islice(seq, mid, len(seq)))

    left, log = mergesort(left, log)
    right, log = mergesort(right, log)

    return merge(left, right, log)


def merge(left, right, log):
    complete = collections.deque()

    while len(left) > 0 and len(right) > 0:
        if log.popleft() == "1":
            complete.append(left.popleft())
        else:
            complete.append(right.popleft())

    complete.extend(left)
    complete.extend(right)

    return complete, log


def checksum(seq):
    result = 1
    for i in xrange(len(seq)):
        result = (31 * result + seq[i]) % 1000003
    return result


if __name__ == "__main__":
    main()
    # cProfile.run('main()')
