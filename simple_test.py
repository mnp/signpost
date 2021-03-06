#!/usr/bin/env python3

import unittest
import simple

facts = [
    [1, (1, 1)],
    [2, (2, 2)],
    [3, (2, 2)],
    [4, (2, 2)],
    [5, (2, 2)],
    [6, (6, 3)],
    [7, (6, 3)],
    [8, (6, 3)],
    [9, (6, 3)],
    [10, (6, 3)],
    [11, (6, 3)],
    [12, (6, 3)],
    [13, (6, 3)],
    [14, (6, 3)],
    [15, (6, 3)],
    [16, (6, 3)],
    [17, (6, 3)],
    [18, (6, 3)],
    [19, (6, 3)],
    [20, (6, 3)],
    [21, (6, 3)],
    [22, (6, 3)],
    [23, (6, 3)],
    [24, (24, 4)],
    [25, (24, 4)],
    [26, (24, 4)],
    [27, (24, 4)],
    [28, (24, 4)],
    [29, (24, 4)],
    [30, (24, 4)],
    [31, (24, 4)],
    [32, (24, 4)],
    [33, (24, 4)],
    [34, (24, 4)],
    [35, (24, 4)],
    [36, (24, 4)],
    [37, (24, 4)],
    [38, (24, 4)],
    [39, (24, 4)],
    [40, (24, 4)],
    [41, (24, 4)],
    [42, (24, 4)],
    [43, (24, 4)],
    [44, (24, 4)],
    [45, (24, 4)],
    [46, (24, 4)],
    [47, (24, 4)],
    [48, (24, 4)],
    [49, (24, 4)],
    [50, (24, 4)],
    [51, (24, 4)],
    [52, (24, 4)],
    [53, (24, 4)],
    [54, (24, 4)],
    [55, (24, 4)],
    [56, (24, 4)],
    [57, (24, 4)],
    [58, (24, 4)],
    [59, (24, 4)],
    [60, (24, 4)],
    [61, (24, 4)],
    [62, (24, 4)],
    [63, (24, 4)],
    [64, (24, 4)],
    [65, (24, 4)],
    [66, (24, 4)],
    [67, (24, 4)],
    [68, (24, 4)],
    [69, (24, 4)],
    [70, (24, 4)],
    [71, (24, 4)],
    [72, (24, 4)],
    [73, (24, 4)],
    [74, (24, 4)],
    [75, (24, 4)],
    [76, (24, 4)],
    [77, (24, 4)],
    [78, (24, 4)],
    [79, (24, 4)],
    [80, (24, 4)],
    [81, (24, 4)],
    [82, (24, 4)],
    [83, (24, 4)],
    [84, (24, 4)],
    [85, (24, 4)],
    [86, (24, 4)],
    [87, (24, 4)],
    [88, (24, 4)],
    [89, (24, 4)],
    [90, (24, 4)],
    [91, (24, 4)],
    [92, (24, 4)],
    [93, (24, 4)],
    [94, (24, 4)],
    [95, (24, 4)],
    [96, (24, 4)],
    [97, (24, 4)],
    [98, (24, 4)],
    [99, (24, 4)],
    [100, (24, 4)],
    [101, (24, 4)],
    [102, (24, 4)],
    [103, (24, 4)],
    [104, (24, 4)],
    [105, (24, 4)],
    [106, (24, 4)],
    [107, (24, 4)],
    [108, (24, 4)],
    [109, (24, 4)],
    [110, (24, 4)],
    [111, (24, 4)],
    [112, (24, 4)],
    [113, (24, 4)],
    [114, (24, 4)],
    [115, (24, 4)],
    [116, (24, 4)],
    [117, (24, 4)],
    [118, (24, 4)],
    [119, (24, 4)],
    [120, (120, 5)],
    [121, (120, 5)],
    [122, (120, 5)],
    [123, (120, 5)],
    [124, (120, 5)],
    [125, (120, 5)],
    [126, (120, 5)],
    [127, (120, 5)],
    [128, (120, 5)],
    [129, (120, 5)],

    ]

# x^y distance m from n
# [ n, (m, x, y) ]
pows = [
    [10, (9, 1, 3, 2)],
    [11, (9, 2, 3, 2)],
    [12, (16, -4, 4, 2)],
    [13, (16, -3, 4, 2)],
    [14, (16, -2, 4, 2)],
    [15, (16, -1, 4, 2)],
    [16, (16, 0, 4, 2)],
    [17, (16, 1, 4, 2)],
    [18, (16, 2, 4, 2)],
    [19, (16, 3, 4, 2)],
    [20, (25, -5, 5, 2)],
    [21, (25, -4, 5, 2)],
    [22, (25, -3, 5, 2)],
    [23, (25, -2, 5, 2)],
    [24, (25, -1, 5, 2)],
    [25, (25, 0, 5, 2)],
    [26, (25, 1, 5, 2)],
    [27, (27, 0, 3, 3)],
    [28, (27, 1, 3, 3)],
    [29, (27, 2, 3, 3)],
    [30, (32, -2, 2, 5)],
    [31, (36, -5, 6, 2)],
    [32, (32, 0, 2, 5)],
    [33, (32, 1, 2, 5)],
    [34, (36, -2, 6, 2)],
    [35, (36, -1, 6, 2)],
    [36, (36, 0, 6, 2)],
    [37, (36, 1, 6, 2)],
    [38, (36, 2, 6, 2)],
    [39, (36, 3, 6, 2)],
    [40, (36, 4, 6, 2)],
    [41, (36, 5, 6, 2)],
    [42, (49, -7, 7, 2)],
    [43, (49, -6, 7, 2)],
    [44, (49, -5, 7, 2)],
    [45, (49, -4, 7, 2)],
    [46, (49, -3, 7, 2)],
    [47, (49, -2, 7, 2)],
    [48, (49, -1, 7, 2)],
    [49, (49, 0, 7, 2)],
    [50, (49, 1, 7, 2)],
    [51, (49, 2, 7, 2)],
    [52, (49, 3, 7, 2)],
    [53, (49, 4, 7, 2)],
    [54, (49, 5, 7, 2)],
    [55, (49, 6, 7, 2)],
    [56, (64, -8, 8, 2)],
    [57, (64, -7, 8, 2)],
    [58, (64, -6, 8, 2)],
    [59, (64, -5, 8, 2)],
    [60, (64, -4, 8, 2)],
    [61, (64, -3, 8, 2)],
    [62, (64, -2, 8, 2)],
    [63, (64, -1, 8, 2)],
    [64, (64, 0, 8, 2)],
    [65, (64, 1, 8, 2)],
    [66, (64, 2, 8, 2)],
    [67, (64, 3, 8, 2)],
    [68, (64, 4, 8, 2)],
    [69, (64, 5, 8, 2)],
    [70, (64, 6, 8, 2)],
    [71, (64, 7, 8, 2)],
    [72, (81, -9, 9, 2)],
    [73, (81, -8, 9, 2)],
    [74, (81, -7, 9, 2)],
    [75, (81, -6, 9, 2)],
    [76, (81, -5, 9, 2)],
    [77, (81, -4, 9, 2)],
    [78, (81, -3, 9, 2)],
    [79, (81, -2, 9, 2)],
    [80, (81, -1, 9, 2)],
    [81, (81, 0, 9, 2)],
    [82, (81, 1, 9, 2)],
    [83, (81, 2, 9, 2)],
    [84, (81, 3, 9, 2)],
    [85, (81, 4, 9, 2)],
    [86, (81, 5, 9, 2)],
    [87, (81, 6, 9, 2)],
    [88, (81, 7, 9, 2)],
    [89, (81, 8, 9, 2)],
    [90, (100, -10, 10, 2)],
    [91, (100, -9, 10, 2)],
    [92, (100, -8, 10, 2)],
    [93, (100, -7, 10, 2)],
    [94, (100, -6, 10, 2)],
    [95, (100, -5, 10, 2)],
    [96, (100, -4, 10, 2)],
    [97, (100, -3, 10, 2)],
    [98, (100, -2, 10, 2)],
    [99, (100, -1, 10, 2)],

]

class TestSimple(unittest.TestCase):
    def runTest(self):
        for (n, expvals) in facts:
            gotvals = simple.largest_fact_less_than(n)
            self.assertEqual(expvals, gotvals, "nearest fact n:{} exp:{} got:{}".format(n, expvals, gotvals))

        for (n, expvals) in pows:
            gotvals = simple.nearest_power(n)
            print (gotvals)
            self.assertEqual(expvals, gotvals, "nearest power n:{} exp:{} got:{}".format(n, expvals, gotvals))

if __name__ == "__main__":
    t = TestSimple()
    t.runTest()
