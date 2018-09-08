#!/usr/bin/env python3

'''Experiment: exhaustively construct all useful signs in the direction of target number'''

import expr
import math
import sys

def construct(target_n):
    todo = []
    memo = {}
    goal = len(str(target_n))

    # Push single digits into memo and work queues
    for i in range (0, 9):
        todo.append((expr.Int(i)))
        memo[i] = i

    while len(todo) > 0:
        item = todo.pop()


    print("todos:")
    print(todo)

    print("memos:")
    print(memo)

if __name__ == "__main__":
    construct(sys.argv[1])
