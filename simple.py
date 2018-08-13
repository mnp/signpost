#!/usr/bin/env

'''
Simplifying assupmtions for first experiment.

  1. As a heuristic, only consider steps (up) towards N. Away from N may be totally valid, but not considered here.  So nearest_to methods will only provide less than N.
  2. Only addititve operation combination operators initially.
  3. A small set of operations.
'''

# from anytree import Node, RenderTree
import math

cache = {}

def fact(n):
    global cache
    if n in cache:
        ans = cache[n]
    elif n < 2:
        ans = 1
        cache[n] = ans
    else:
        ans = 1
        for i in range(2, n+1):
            ans *= i
        cache[n] = ans
    return ans

def nearest_power_less_than(n, target):
    best_m = n
    kmax = int(math.log(n, 2)) + 1

    # minimize m: the distance from n
    for k in range(2, kmax):
        x = math.floor(n ** (1/k))     # a root
        m = abs(target - math.pow(x, k))
        if m < best_m:
            best_m = m
            best_k = k
            best_x = x

    # x^k is m distance from n
    return (int(best_m), best_x, best_k)

def nearest_power(n):
    (m1, x1, k1) = nearest_power_less_than(n, n)
    (m2, x2, k2) = nearest_power_less_than(n + m1 + 1, n)

    if m1 < m2:
        return (m1, x1, k1)
    else:
        return (m2, x2, k2)

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
    return (best_m, best_fact)

class Operation:
    def __init__(self):
        self.foo = 1

    def cost(self):
        return len(this.toStr)

class OpPow(Operation):
    def __init__(self, x, y):
        this.x = x
        this.y = y
        this.n = pow(x, y)

    def toStr(self):
        return "{}^{}".format(this.x, this.y)

class OpFact(Operation):
    def __init__(self, n):
        out=n
        while(n>1):
            out *= n
            n -= 1
        self.n = out

    def toStr(self):
        return "{}!".format(self.n)

if __name__ == "__main__":

#    for i in range(1, 130):
#        z = largest_fact_less_than(i)
#        print("[{}, ({}, {})],".format(i, z[0], z[1]))

    for i in range(10, 100):
        z = nearest_power_less_than(i, i)
        print("    [{}, ({}, {}, {})],".format(i, z[0], z[1], z[2]))
