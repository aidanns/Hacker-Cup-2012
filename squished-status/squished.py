import sys


def main():

    tokens = []

    for line in sys.stdin.readlines():
        for token in line.split():
            tokens.append(token)

    num_cases = int(tokens.pop(0))

    for case_num in xrange(1, num_cases + 1):
        print "Case #" + str(case_num) + ": " + str(squish(tokens.pop(0), tokens.pop(0)))

    # print "Ready!"


# number (string) largest number that is used as a character in this encoding.
# encoded (string) encoded string representing a string of chars
#
# return (int) number of possible valid char strings this could represent.
def squish(number, encoded):

    max_code = int(number)
    encoded = [int(n) for n in encoded]

    perms = [0 for n in encoded]

    mod = 4207849484

    for i in xrange(len(encoded) - 1, -1, -1):

        # how many permutations there are from this digit onwards.
        one = 0
        two = 0
        three = 0

        # there's always space for a single digit number
        # if the single digit here is within the allowable range
        if encoded[i] <= max_code and encoded[i] != 0:
            # if there is more of the string after this
            if i + 1 < len(encoded):
                one = perms[i + 1]
            else:
                one = 1
        # else:
        #     # if this is the first one, then we're screwed
        #     if i == 0:
        #         return 0
        #     else:
        #         # if we can't get a single digit out, then we won't be able to get a 2 or 3
        #         perms[i] = 0
        #         continue

        # if there is space for a 2 digit number
        if i + 1 < len(encoded):
            # if the two digit number is within the allowable range
            if encoded[i] * 10 + encoded[i + 1] <= max_code and encoded[i] != 0:
                # if there is more of the string after this
                if i + 2 < len(encoded):
                    two = perms[i + 2]
                else:
                    two = 1
            # else:
            #     # if this is the first digit, then we can't make anything
            #     if i == 0:
            #         return one
            #     else:
            #         # if we can't get two digits out, then we can't get three
            #         perms[i] = one
            #         continue

        # if there is space for a 3 digit number starting here
        if i + 2 < len(encoded):
            # if the three digit number is within the allowable range
            if encoded[i] * 100 + encoded[i + 1] * 10 + encoded[i + 2] <= max_code and encoded[i] != 0:
                # if there is more of the sting after this 3 digit number
                if i + 3 < len(encoded):
                    three = perms[i + 3]
                else:
                    three = 1
            # else:
            #     # if this is the first digit, then we can't make anything
            #     if i == 0:
            #         return (one + two) % mod
            #     else:
            #         perms[i] = (one + two) % mod
            #         continue

        perms[i] = (one + two + three) % mod
        # print str(perms[i]) + " permutations from position " + str(i)

    return perms[0]

if __name__ == "__main__":
    main()
