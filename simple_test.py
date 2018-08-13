import unittest
import simple

facts = [
    [1,    (1, 1)],
    [2,    (2, 2)],
    [3,    (2, 2)],
    [4,    (2, 2)],
    [5,    (2, 2)],
    [6,    (3, 6)],
    [7,    (3, 6)],
    [8,    (3, 6)],
    [9,    (3, 6)],
    [10,   (3, 6)],
    [11,   (3, 6)],
    [12,   (3, 6)],
    [13,   (3, 6)],
    [14,   (3, 6)],
    [15,   (3, 6)],
    [16,   (3, 6)],
    [17,   (3, 6)],
    [18,   (3, 6)],
    [19,   (3, 6)],
    [20,   (3, 6)],
    [21,   (3, 6)],
    [22,   (3, 6)],
    [23,   (3, 6)],
    [24,   (4, 24)],
    [25,   (4, 24)],
    [26,   (4, 24)],
    [118,  (4, 24)],
    [119,  (4, 24)],
    [120,  (5, 120)],
    [121,  (5, 120)],
    [719,  (5, 120)],
    [720,  (6, 720)],
    [721,  (6, 720)],
    [5039, (6, 720)],
    [5040, (7, 5040)],
    [5041, (7, 5040)],
    ]

# x^y distance m from n
# [ n, (m, x, y) ]
pows = [
    [10, (1, 3, 2)],
    [11, (2, 3, 2)],
    [12, (3, 3, 2)],
    [13, (3, 4, 2)],
    [14, (2, 4, 2)],
    [15, (1, 4, 2)],
    [16, (0, 4, 2)],
    [17, (1, 4, 2)],
    [18, (2, 4, 2)],
    [19, (3, 4, 2)],
    [20, (4, 2, 4)],
    [21, (4, 5, 2)],
    [22, (3, 5, 2)],
    [23, (2, 5, 2)],
    [24, (1, 5, 2)],
    [25, (0, 5, 2)],
    [26, (1, 5, 2)],
    [27, (0, 3, 3)],
    [28, (1, 3, 3)],
    [29, (2, 3, 3)],
    [30, (2, 2, 5)],
    [31, (1, 2, 5)],
    [32, (0, 2, 5)],
    [33, (1, 2, 5)],
    [34, (2, 6, 2)],
    [35, (1, 6, 2)],
    [36, (0, 6, 2)],
    [37, (1, 6, 2)],
    [38, (2, 6, 2)],
    [39, (3, 6, 2)],
    [40, (4, 6, 2)],
    [41, (5, 6, 2)],
    [42, (6, 6, 2)],
    [43, (6, 7, 2)],
    [44, (5, 7, 2)],
    [45, (4, 7, 2)],
    [46, (3, 7, 2)],
    [47, (2, 7, 2)],
    [48, (1, 7, 2)],
    [49, (0, 7, 2)],
    [50, (1, 7, 2)],
    [51, (2, 7, 2)],
    [52, (3, 7, 2)],
    [53, (4, 7, 2)],
    [54, (5, 7, 2)],
    [55, (6, 7, 2)],
    [56, (7, 7, 2)],
    [57, (7, 8, 2)],
    [58, (6, 8, 2)],
    [59, (5, 8, 2)],
    [60, (4, 8, 2)],
    [61, (3, 8, 2)],
    [62, (2, 8, 2)],
    [63, (1, 8, 2)],
    [64, (0, 8, 2)],
    [65, (1, 8, 2)],
    [66, (2, 8, 2)],
    [67, (3, 8, 2)],
    [68, (4, 8, 2)],
    [69, (5, 8, 2)],
    [70, (6, 8, 2)],
    [71, (7, 8, 2)],
    [72, (8, 4, 3)],
    [73, (8, 9, 2)],
    [74, (7, 9, 2)],
    [75, (6, 9, 2)],
    [76, (5, 9, 2)],
    [77, (4, 9, 2)],
    [78, (3, 9, 2)],
    [79, (2, 9, 2)],
    [80, (1, 9, 2)],
    [81, (0, 9, 2)],
    [82, (1, 9, 2)],
    [83, (2, 9, 2)],
    [84, (3, 9, 2)],
    [85, (4, 9, 2)],
    [86, (5, 9, 2)],
    [87, (6, 9, 2)],
    [88, (7, 9, 2)],
    [89, (8, 9, 2)],
    [90, (9, 3, 4)],
    [91, (9, 10, 2)],
    [92, (8, 10, 2)],
    [93, (7, 10, 2)],
    [94, (6, 10, 2)],
    [95, (5, 10, 2)],
    [96, (4, 10, 2)],
    [97, (3, 10, 2)],
    [98, (2, 10, 2)],
    [99, (1, 10, 2)],
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
