#!/usr/bin/env python3

'''
Simplifying assupmtions for first experiment.

  1. As a heuristic, only consider steps (up) towards N. Away from N may be totally valid, but not considered here.  So nearest_to methods will only provide less than N.
  2. Only addititve operation combination operators initially.
  3. A small set of operations.
'''

from anytree import Node, RenderTree
import math

fact_cache = {}

def fact(n):
    global fact_cache
    if n in fact_cache:
        ans = fact_cache[n]
    elif n < 2:
        ans = 1
        fact_cache[n] = ans
    else:
        ans = 1
        for i in range(2, n+1):
            ans *= i
        fact_cache[n] = ans
    return ans

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

power_cache = {}

# Bad, but good enough to get the tree search working, then...
# TODO: Best algorithm here
# https://math.stackexchange.com/questions/298044/given-an-integer-how-can-i-detect-the-nearest-integer-perfect-power-efficiently#2219230
def nearest_power(n):
    global power_cache
    if n in power_cache:
        return power_cache[n]

    (z1, m1, x1, k1) = nearest_power_less_than(n, n)
    (z2, m2, x2, k2) = nearest_power_less_than(n + m1 + 1, n)

    if m1 < m2:
        power_cache[n] = (z1, m1, x1, k1)
        return (z1, m1, x1, k1)
    else:
        power_cache[n] = (z2, m2, x2, k2)
        return (z2, m2, x2, k2)

def largest_fact_less_than(n):
    best_m = n
    best_fact = 1

    if n >= 24:
        for i in range(2, int(math.sqrt(n))+1):
            fact_i = fact(i)
            if fact_i <= n:
                best_m = i
                best_fact = fact_i
            else:
                break
    elif n >= 6:
        best_m = 3
        best_fact = 6
    elif n >= 2:
        best_m = 2
        best_fact = 2
    return (best_fact, best_m)

def gen_fact():
    for i in range(1, 130):
        z = largest_fact_less_than(i)
        print("    [{}, {}],".format(i, str(z)))

def gen_pow():
    for i in range(10, 100):
        z = nearest_power(i)
        print("    [{}, {}],".format(i, z))

class Operation:
    def __init__(self, val, n, m):
        self.n = n
        self.m = m
        self.val = val
        self.cost = len(self.toStr())

class OpPow(Operation):
    def __init__(self, n):
        (val, m, self.x, self.y) = nearest_power(n)
        super().__init__(val, n, m)

    def toStr(self):
        return "{}^{}".format(self.x, self.y)

class OpFact(Operation):
    def __init__(self, n):
        (val, m) = largest_fact_less_than(n)
        super().__init__(val, n, m)

    def toStr(self):
        return "{}!".format(self.m)

class OpIdentity(Operation):
    def __init__(self, n):
        super().__init__(n, n, 0)

    def toStr(self):
        return "{}".format(self.n)

allfuncs = [
    OpFact,
    OpPow
]

if __name__ == "__main__":
    gen_pow()

if __name__ == "__main__z":
    n = 40
    x = OpIdentity(n)

    root = Node("root", op=x)

    for op in allfuncs:
        x = op(n)
        Node(x.toStr(), parent=root, op=x)

    for pre, fill, node in RenderTree(root):
        print("%s%s  %s %s" % (pre, node.name, node.op.n, node.op.val))
