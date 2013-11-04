import random
import sys


def main():

    print str(10)
    for i in xrange(10):
        seq, log = generate(10000)
        print "10000 " + "".join(log)
        print >> sys.stderr, str(seq)

    # print "Ready!"


# sequence_length (int) the number of sequential integers in the sequence
# log (string) log of 1's and 2's. 1 = <, 2 = >
#
# return (int) the question specific hash of the resulting sequence
def generate(sequence_length):
    seq = range(1, sequence_length + 1)
    random.shuffle(seq)
    _, log = mergesort(seq, [])
    return seq, log


def mergesort(seq, log):

    if len(seq) == 1:
        return seq, log

    mid = len(seq) / 2
    left = seq[:mid]
    right = seq[mid:]

    left, log = mergesort(left, log)
    right, log = mergesort(right, log)

    return merge(left, right, log)


def merge(left, right, log):
    complete = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            complete.append(left.pop(0))
            log.append("1")
        else:
            complete.append(right.pop(0))
            log.append("2")

    complete = complete + left + right

    return complete, log


if __name__ == "__main__":
    main()
