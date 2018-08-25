#!/usr/bin/env python3

# might need
#  LANG=en_US.utf8  or LANG=UTF-8 on osx?

import math
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
        self.n = n
        super().__init__(str(n))

    def toStr(self):
        return str(self.n)

class Neg(Expr1):
    def __init__(self, a):
        super().__init__("neg", a)
        self.n = -a.n

class Fact(Expr1):
    def __init__(self, a):
        super().__init__("fact", a)
        self.n = math.factorial(a.n)

class Mul(Expr2):
    def __init__(self, a, b):
        super().__init__("mul", a, b)
        self.n = a.n * b.n

class Pow(Expr2):
    def __init__(self, a, b):
        super().__init__("pow", a, b)
        self.n = a.n ** b.n

class Add(Expr2):
    def __init__(self, a, b):
        super().__init__("add", a, b)
        self.n = a.n + b.n

root = Mul(Neg(Pow(Int(4), Int(5))), Fact(Add(Int(1), Int(2))))

for pre, fill, node in RenderTree(root):
    print("{}{} \t n={}".format(pre, node.name, node.n))
print()

# wrong - toStr() descends dfs
#for node in PreOrderIter(root):
#    print(node.toStr())

# good
print(root.toStr())
