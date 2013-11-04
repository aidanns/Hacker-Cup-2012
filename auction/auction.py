import sys


def main():
    num_cases = int(sys.stdin.readline())

    for j in range(num_cases):
        case_num = j + 1
        line = sys.stdin.readline()
        (num_items, price, weight, m, k, a, b, c, d) = [int(x) for x in line.split()]

        # print "# Items: " + str(num_items)
        # print "Price: " + str(price)
        # print "Weight: " + str(weight)
        # print "m: " + str(m)
        # print "k: " + str(k)
        # print "a: " + str(a)
        # print "b: " + str(b)
        # print "c: " + str(c)
        # print "d: " + str(d)

        a = a % m
        c = c % k
        b = b % m
        d = d % k

        terrible = [(price, weight)]
        bargain = [(price, weight)]

        orig_price = price
        orig_weight = weight

        price_difference = ((price * a + b) % m) + 1 - price
        weight_difference = ((weight * c + d) % k) + 1 - weight

        i = 0
        while i < num_items:  # we've already calculated the first one

            if i % 10000 == 0:
                print "Generated " + str(i) + " items so far"

            if price == orig_price and weight == orig_weight:
                print "Looped at index " + str(i)

            # print "Price: " + str(price) + " Weight: " + str(weight)

            price = (price + price_difference) % m
            weight = (weight + weight_difference) % k

            new_terribles = []
            new_bargains = []

            is_bargain = True
            is_terrible = True

            for index, (p2, w2) in enumerate(bargain):
                if not ((price < p2 and weight <= w2) or (price == p2 and weight < w2)):
                    new_bargains.append((p2, w2))
                else:
                    is_terrible = False

            # print "Bargain: " + str(bargain)

            for index, (p2, w2) in enumerate(terrible):
                if not ((p2 < price and w2 <= weight) or (price == p2 and w2 < weight)):
                    new_terribles.append((p2, w2))
                else:
                    is_bargain = False

            if (is_bargain):
                new_bargains.append((price, weight))
            if (is_terrible):
                new_terribles.append((price, weight))

            bargain = new_bargains
            terrible = new_terribles

            i = i + 1

        print "Case #" + str(case_num) + ": " + str(len(terrible)) + " " + str(len(bargain))

if __name__ == '__main__':
    main()
