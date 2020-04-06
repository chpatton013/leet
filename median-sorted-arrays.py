#!/usr/bin/env python3

import math
from typing import *


TEST_CASES = [
    ([4, 20, 32, 50, 55, 61], [1, 15, 22, 30, 70],),
    ([1, 2], [3],),
    ([1], [2, 3],),
    ([1, 2], [3, 4],),
]


class Constraints:
    def __init__(self, a: List[int], b: List[int]):
        self.lhs_count = int((len(a) + len(b) + 1) / 2)
        self.a_min_count = 0
        self.a_max_count = len(a)

    @property
    def a_count(self):
        return int((self.a_min_count + self.a_max_count) / 2)

    @property
    def b_count(self):
        return self.lhs_count - self.a_count


def maximum(x, y):
    if x is None: return y
    if y is None: return x
    return max(x, y)


def minimum(x, y):
    if x is None: return y
    if y is None: return x
    return min(x, y)


def greater_than(x, y):
    if x is None: return False
    if y is None: return False
    return x > y


class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        # Swap lists so `a` is always the shortest.
        if len(a) > len(b):
            a, b = b, a

        c = Constraints(a, b)

        while c.a_min_count <= c.a_max_count:
            x = a[c.a_count - 1] if c.a_count > 0 else None
            y = b[c.b_count - 1] if c.b_count > 0 else None
            x_next = a[c.a_count] if c.a_count < len(a) else None
            y_next = b[c.b_count] if c.b_count < len(b) else None

            if greater_than(x, y_next):
                # Tighten search range by decreasing `a`s maximum contribution.
                c.a_max_count = c.a_count - 1
            elif greater_than(y, x_next):
                # Tighten search range by increasing `a`s minimum contribution.
                c.a_min_count = c.a_count + 1
            else:
                # Found the median; either x, y, or their mid-point.
                greatest_lhs = maximum(x, y)
                if (len(a) + len(b)) % 2:
                    return greatest_lhs
                else:
                    lowest_rhs = minimum(x_next, y_next)
                    return (greatest_lhs + lowest_rhs) / 2

        raise RuntimeError()


if __name__ == "__main__":
    for case in TEST_CASES:
        print("=" * 40)
        print("case", case)
        print("result", Solution().findMedianSortedArrays(*case))
        print("-" * 40)
