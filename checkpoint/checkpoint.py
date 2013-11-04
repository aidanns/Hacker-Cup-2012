import sys
from collections import defaultdict
import math


kCacheSize = 5000
kMaxPerms = 10000000


def main():
    num_cases = int(sys.stdin.readline())

    for case_num in range(1, num_cases + 1):
        line = sys.stdin.readline()
        s = int(line)

        print "Case #" + str(case_num) + ": " + str(checkpoint(s))
    # print "Ready!"


def checkpoint(s):

    paths = []

    for (first, second) in factorise(s):
        paths.append(shortest_path_for_perms(first) + shortest_path_for_perms(second))

    paths.sort()
    return paths[0]


def perms(x, y):
    if cache[x][y] == -1:
        cache[x][y] = perms(x - 1, y) + perms(x, y - 1)
        cache[y][x] = perms(x - 1, y) + perms(x, y - 1)
    return cache[x][y]

# Setup the cache.
cache = [[-1] * kCacheSize for x in xrange(kCacheSize)]
for i in xrange(kCacheSize):
    cache[0][i] = 1
    cache[1][i] = i + 1
    cache[i][0] = 1
    cache[i][1] = i + 1

# maps num permutations to length of the shortest path
reverse_cache = defaultdict(int)


def prepare_caches():

    global cache
    global reverse_cache

    i = 2
    j = 2

    while i < kCacheSize:
        while j < kCacheSize:
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
            if reverse_cache[cache[i][j]] == 0 or reverse_cache[cache[i][j]] > i * j:
                reverse_cache[cache[i][j]] = i + j
            if cache[i][j] > kMaxPerms:
                break
            j = j + 1
        i = i + 1
        j = 2


prepare_caches()


def shortest_path_for_perms(p):
    if reverse_cache[p] == 0:
        # not in the cache.
        return p

    return reverse_cache[p]


def factorise(n):

    result = []

    for i in xrange(1, (int)(math.ceil(math.sqrt(n) + 1))):
        if n % i == 0:
            result.append((i, n / i))

    return result


if __name__ == '__main__':
    main()
