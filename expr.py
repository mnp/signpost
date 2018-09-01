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

    def sexprStr(self):
        return "({} {})".format(self.name, self.a.sexprStr())

class Expr2(Expr):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.children = [a,  b]
        self.a = a
        self.b = b

    def sexprStr(self):
        return "({} {} {})".format(self.name, self.a.sexprStr(), self.b.sexprStr())

    def infixStr(self):
        return "{}{}{}".format(self.a.infixStr(), self.name, self.b.infixStr())

class Int(Expr):
    '''"Terminals are different - node created here and stitched into parent here.'''
    def __init__(self, n):
        super().__init__(str(n))
        self.n = n

    def sexprStr(self):
        return str(self.n)

    def infixStr(self):
        return str(self.n)

class Neg(Expr1):
    def __init__(self, a):
        super().__init__("neg", a)

    def infixStr(self):
        return "-" + self.a.infixStr()

class Fact(Expr1):
    def __init__(self, a):
        super().__init__("fact", a)

    def infixStr(self):
        return self.a.infixStr() + "!"

class Mul(Expr2):
    def __init__(self, a, b):
        super().__init__("*", a, b)

class Pow(Expr2):
    def __init__(self, a, b):
        super().__init__("^", a, b)

class Add(Expr2):
    def __init__(self, a, b):
        super().__init__("+", a, b)

    def infixStr(self):
        return "{} {} {}".format(self.a.infixStr(), self.name, self.b.infixStr())

class Alt(Expr):
    def __init__(self, alternates):
        self.children = alternates
        self.name = "alternates"

    def sexprStr(self):
        return "\n".join([x.sexprStr() for x in self.children])

    def infixStr(self):
        return "\n".join([x.infixStr() for x in self.children])

def reduce_power(target_n):
    (n, remainder, x, y) = simple.nearest_power(target_n)
    if remainder > 0:
        return Add(Pow(Int(x), Int(y)), reduce_int(remainder))
    else:
        return Pow(Int(x), Int(y))

def reduce_fact(target_n):
    (coeff, fact, n, remainder) = simple.largest_fact_less_than(target_n)
    if coeff > 1:
        term = Mul(Int(coeff), Fact(Int(n)))
    else:
        term = Fact(Int(n))
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

    # good - each expr's sexprStr() descends dfs (tree might not be necessary for this part)
    print(root.sexprStr())

root = reduce_int(int(sys.argv[1]))

print( root.infixStr() )

print("-----")
print( root.sexprStr() )
print("-----")

for pre, fill, node in RenderTree(root):
#     print(node.infixStr())
    print("{}{} ".format(pre, node.name))
