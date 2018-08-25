#!/usr/bin/env python3

'''
Simplifying assupmtions for first experiment.

  1. As a heuristic, only consider steps (up) towards N. Away from N may be totally valid, but not considered here.  So nearest_to methods will only provide less than N.
  2. Only addititve operation combination operators initially.
  3. A small set of operations.
'''

# might need
#  LANG=en_US.utf8  or LANG=UTF-8 on osx?

from anytree import Node, RenderTree, PreOrderIter

import functools
import math
import sys
import time

def nearest_power_less_than(n, target):
    best_m = n
    kmax = int(math.floor(math.log(n, 2)))
    z = 0

    # minimize m: the distance from n
    for k in range(2, kmax + 1):
        x = math.floor(math.pow(n, 1.0/k))
        z = math.pow(x, k)
        m = target - z
        if abs(m) < best_m:
            best_m = m
            best_k = k
            best_x = x
            best_z = z

    # x^k is m distance from n
    return (int(best_z), int(best_m), int(best_x), best_k)


# Bad, but good enough to get the tree search working, then...
# TODO: Best algorithm here
# https://math.stackexchange.com/questions/298044/given-an-integer-how-can-i-detect-the-nearest-integer-perfect-power-efficiently#2219230
@functools.lru_cache(maxsize=None)
def nearest_power(n):
    (z1, m1, x1, k1) = nearest_power_less_than(n, n)
    (z2, m2, x2, k2) = nearest_power_less_than(n + m1 + 1, n)
    if m1 < m2:
        return (z1, m1, x1, k1)
    else:
        return (z2, m2, x2, k2)

@functools.lru_cache(maxsize=None)
def largest_fact_less_than(target):
    '''Returns (a, n, r) such that an! + r = target'''
    best_r = target
    best_fact = 1
    best_n = 0

    if target >= 24:
        for n in range(4, int(math.sqrt(target))+1):
            # sterling = math.sqrt( 2 * math.pi * n) * (n/math.e)**n
            tryfact = math.factorial(n)
            if tryfact <= target:
                best_fact = tryfact
                best_r = target - tryfact
                best_n = n
            else:
                break
    elif target >= 6:
        best_r = target - 6
        best_fact = 6
        best_n = 3
    elif target >= 2:
        best_r = target - 2
        best_fact = 2
        best_n = 2

    # Now, how about multiples, ie: n = ax! + r
    if best_fact < best_r:
        mult = math.floor(target / best_fact)
        best_r = target - mult * best_fact
    else:
        mult = 1
    return (mult, best_fact, best_n, best_r)

class Operation:
    def __init__(self, a, n, r):
        self.n = int(n)         # current target, starts as N at root
        self.a = int(a)         # multiple
        self.r = int(r)         # distance to n
        self.cost = len(self.toStr())

class OpPow(Operation):
    name = "pow"
    func = nearest_power

    def __init__(self, n):
        (val, r, self.x, self.y) = nearest_power(n)
        super().__init__(1, abs(n-val), r)

    def toStr(self):
        if self.a > 1:
            astr = str(self.a) + " * "
        else:
            astr = ''
        return "{}{}^{}".format(astr, self.x, self.y)

class OpFact(Operation):
    name = "fact"
    func = largest_fact_less_than

    def __init__(self, n):
        (a, f, x, r) = largest_fact_less_than(n)
        self.x = x
        super().__init__(a, abs(n-f), r)

    def toStr(self):
        if self.a > 1:
            astr = str(self.a) + " * "
        else:
            astr = ''
        return "{}{}!".format(astr, self.x)

class OpIdentity(Operation):
    def __init__(self, n):
        super().__init__(n, n, 0)

    def toStr(self):
        return "{}".format(self.n)

allfuncs = [
    OpFact,
    OpPow
]

def gen_fact():
    for i in range(1, 130):
        z = largest_fact_less_than(i)
        print("    [{}, {}],".format(i, str(z)))

def gen_pow():
    for i in range(10, 100):
        z = nearest_power(i)
        print("    [{}, {}],".format(i, z))

def dump_caches():
    fmt = "{}\t{}"
    print(fmt.format("Func", "Cache Info"))
    print(fmt.format("----", "----------"))
    for f in allfuncs:
        print(fmt.format(f.name, f.func.cache_info()))

# How to balance cost vs m?
def reduce_knapsack(op, node):
    if op.n < 10:
        return

    tryfuncs = []
    for func in allfuncs:
        newop = func(op.n)
        tryfuncs.append(newop)

    best_cost = op.n
    for func in tryfuncs:
        if func.cost < best_cost:
            best_cost = func.cost
            best_func = func

    newnode = Node(best_func.toStr(), parent=node, op=best_func)
    reduce_knapsack(best_func, newnode)

def reduce_full(op, node):
    if op.n < 10:
        return
    for func in allfuncs:
        newop = func(op.n)
        newnode = Node(newop.toStr(), parent=node, op=newop)
        reduce_full(newop, newnode)
        # TODO: reduce x, y, and m for pow
        # TODO: more combiner ops than +

def main(n):
    rootop = OpIdentity(n)
    rootnode = Node("root", op=rootop)
    reduce_full(rootop, rootnode)
    for pre, fill, node in RenderTree(rootnode):
        print("{}{} n:{} r:{} a:{}".format(pre, node.name, node.op.n, node.op.r, node.op.a))

    best_soln = ''
    best_slen = 999999
    for node in PreOrderIter(rootnode):
        if node.is_leaf:
            terms = [ pathnode.name for pathnode in node.path ][1:]
            if node.op.n > 0:
                terms += [str(node.op.n)]
            soln = " + ".join(terms)
`            slen = len(soln)
            if slen < best_slen:
                best_soln = soln
                best_slen = slen

            print("{:>3}: {}".format(slen, soln))

    print()
    print(best_soln)

def expr_experiment():
    # 1 * 2! - 3 * 4^5 + 1

    root = Node("N")
    plus = Node("+", parent=root)
    t1   = Node("*", parent=plus)
    one  = Node("1", parent=t1)
    bang = Node("!", parent=t1)
    two  = Node("2", parent=bang)
    t2   = Node("*", parent=plus)
    t2m  = Node("3", parent=t2)
    fxy  = Node("^", parent=t2m)
    four = Node("4", parent=fxy)
    four = Node("5", parent=fxy)
    one  = Node("1", parent=plus)

    for pre, fill, node in RenderTree(root):
        print("{}{}".format(pre, node.name))

if __name__ == "__main__":
    start = time.time()
    main(sys.argv[1])
    end = time.time()
    print()
    print("%0.2f sec " % (end - start))
    print()
    dump_caches()

#    print(largest_fact_less_than(50))
#    gen_fact()
