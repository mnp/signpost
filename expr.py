#!/usr/bin/env python3

# might need
#  LANG=en_US.utf8  or LANG=UTF-8 on osx?

import math
import simple
import sys

from anytree import Node, RenderTree, PreOrderIter, NodeMixin

class ExprBase(object):
    def __init__(self, name):
        self.name = name

class Expr(ExprBase, NodeMixin):
    def __init__(self, name, parent=None):
        super().__init__(name)
        self.parent = parent

class Expr1(Expr):
    def __init__(self, name, a):
        super().__init__(name)
        self.a = a
        self.children = [a]

    def toStr(self):
        return "({} {})".format(self.name, self.a.toStr())

class Expr2(Expr):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.children = [a,  b]
        self.a = a
        self.b = b

    def toStr(self):
        return "({} {} {})".format(self.name, self.a.toStr(), self.b.toStr())

class Int(Expr):
    '''"Terminals are different - node created here and stitched into parent here.'''
    def __init__(self, n):
        super().__init__(str(n))
        self.n = n

    def toStr(self):
        return str(self.n)

class Neg(Expr1):
    def __init__(self, a):
        super().__init__("neg", a)

class Fact(Expr1):
    def __init__(self, a):
        super().__init__("fact", a)

class Mul(Expr2):
    def __init__(self, a, b):
        super().__init__("mul", a, b)

class Pow(Expr2):
    def __init__(self, a, b):
        super().__init__("pow", a, b)

class Add(Expr2):
    def __init__(self, a, b):
        super().__init__("add", a, b)

class Alt(Expr):
    def __init__(self, alternates):
        self.alternates = alternates

    def toStr(self):
        return [x.toStr() for x in self.alternates]

def reduce_power(target_n):
    (n, remainder, x, y) = simple.nearest_power(target_n)
    return Add(Pow(Int(x), Int(y)), reduce_int(remainder))

def reduce_fact(target_n):
    (coeff, fact, n, remainder) = simple.largest_fact_less_than(target_n)
    inner = Fact(Int(n))
    if coeff > 1:
        term = Mul(Int(coeff), inner)
    else:
        term = inner
    if remainder > 0:
        return Add(term, reduce_int(remainder))
    else:
        return term

OPERATIONS = [reduce_power, reduce_fact]

def reduce_int(n):
    '''examine an int, returning an expr'''
    if n < 0:
        return Neg(reduce_int(- n))

    if n <= 10:
        return Int(n)

    exprs = []
    for op in OPERATIONS:
        exprs += [op(n)]
    return Alt(exprs)

def expr_test():
    root = Mul(Neg(Pow(Int(4), Int(5))), Fact(Add(Int(1), Int(2))))

    for pre, fill, node in RenderTree(root):
        print("{}{} \t n={}".format(pre, node.name, node.n))
    print()

    # good - each expr's toStr() descends dfs (tree might not be necessary for this part)
    print(root.toStr())

#for node in reduce_int(44):
#    print(node.toStr())

print( reduce_int(int(sys.argv[1])).toStr() )
