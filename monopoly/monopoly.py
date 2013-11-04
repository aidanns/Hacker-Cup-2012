import sys


def main():

    num_cases = int(sys.stdin.readline().strip())

    # consume the blank line
    sys.stdin.readline()

    for case_num in xrange(1, num_cases + 1):

        num_employees, branching_factor = tuple([int(x) for x in sys.stdin.readline().strip().split()])
        merges = []

        while (True):
            line = sys.stdin.readline()
            if line == "" or line == "\n":
                break
            merges.append(tuple([int(x) for x in line.strip().split()]))

        print "Case #" + str(case_num) + ": " + str(monopoly(num_employees, branching_factor, merges))


def monopoly(num_employees, branching_factor, merges):
    employees = [0]  # no zero employee
    for employee in xrange(1, num_employees + 1):
        employees.append(Tree(employee))

    for (left, right) in merges:
        merge(employees[left].organisation(), employees[right].organisation(), branching_factor)

    return employees[1].organisation()
    # print str(employees[1].organisation())
    # return employees[1].organisation().depth()


def merge(left, right, branching_factor):
    if (left.depth() > right.depth() and left.num_children() < branching_factor):
        # print "Adding " + str(right) + " as a child of " + str(left)
        left.add_child(right)
    elif right.num_children() < branching_factor:
        # print "Adding " + str(left) + " as a child of " + str(right)
        right.add_child(left)
    elif left.num_children() < branching_factor:
        left.add_child(right)
    else:
        print "Can't merge " + str(left) + " and " + str(right)

    return


class Tree:
    def __init__(self, number):
        self.number = number
        self.children = []
        self.parent = self

    def __str__(self):
        s = "(" + str(self.number)
        for c in self.children:
            s = s + " " + str(c)
        s = s + ")"
        return s

    def organisation(self):
        org = self
        while org.parent != org:
            org = org.parent
        return org

    def depth(self):
        if len(self.children) == 0:
            return 1
        else:
            return 1 + max([c.depth() for c in self.children])

    def num_children(self):
        return len(self.children)

    def add_child(self, other):
        self.children.append(other)
        other.parent = self

    def reorg_possible(self, free_required, branching_factor):
        if free_required > branching_factor:
            return False
        if branching_factor - self.num_children() >= free_required:
            return True
        for child_index, child in enumerate(self.children):
            num_right_sibling = self.num_children() - 1 - child_index
            if child.reorg_possible(free_required + 1 + num_right_sibling, branching_factor):
                return True
        return False

    def reorg(self, free_required, branching_factor):
        # assume that it's possible
        if branching_factor - self.num_children() >= free_required:
            return
        depth = []
        for child_index, child in enumerate(self.children):
            num_right_sibling = self.num_children() - 1 - child_index
            if child.reorg_possible(free_required + 1 + num_right_sibling, branching_factor):
                new_child = child.reorg(free_required + 1 + num_right_sibling, branching_factor)
                new_child.add_child(self)
                for r in self.children[child_index + 1:self.num_children()]:
                    new_child.add_child(r)
                self.children = self.children[0:child_index]

                new_child.paren = self.parent

        for c in self.children:
            if c.reorg_possible():
                depth.append(c.depth())
            else:
                depth.append(50000)  # bigger than the largest possible depth

        child_index = self.children.index(min(depth))
        self.children[child_index].reorg(free_required + 1, branching_factor)
        return new_child


if __name__ == "__main__":
    main()
