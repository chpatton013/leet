#!/usr/bin/env python3

from typing import List, Optional, Tuple


class Match:
    def match(self, s: str, i: int) -> Tuple[bool, int]:
        raise RuntimeError()
    def backtrack(self) -> Optional[int]:
        raise RuntimeError()


class SingleMatch(Match):
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

    def match(self, s: str, i: int) -> Tuple[bool, int]:
        if i >= len(s):
            return False, i
        elif self.char in (".", s[i]):
            return (True, i + 1)
        else:
            return (False, i)

    def backtrack(self) -> Optional[int]:
        return None


class RepeatMatch(Match):
    def __init__(self, char):
        self.char = char
        self.begin_s_index = -1
        self.end_s_index = -1

    def __str__(self):
        return self.char + "*"

    def match(self, s: str, i: int) -> Tuple[bool, int]:
        self.begin_s_index = i
        while (i < len(s)) and (self.char in (".", s[i])):
            i += 1
        self.end_s_index = i
        return (True, i)

    def backtrack(self) -> Optional[int]:
        if self.end_s_index > self.begin_s_index:
            self.end_s_index -= 1
            return self.end_s_index
        else:
            return None


def next_match(p: str, i: int) -> Tuple[str, bool, int]:
    if (i + 1 < len(p)) and (p[i + 1] == "*"):
        return (RepeatMatch(p[i]), i + 2)
    else:
        return (SingleMatch(p[i]), i + 1)


def make_matches(p: str) -> List[Match]:
    matches = []
    p_index = 0
    while p_index < len(p):
        match, p_index = next_match(p, p_index)
        matches.append(match)
    return matches


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = make_matches(p)

        s_index = 0
        match_index = 0
        while s_index < len(s) or match_index < len(m):
            if match_index == len(m):
                # We ran out of matches before reaching the end of the string.
                return False

            is_match, s_index = m[match_index].match(s, s_index)
            if not is_match:
                while match_index >= 0:
                    s_index = m[match_index].backtrack()
                    if s_index is not None:
                        break
                    match_index -= 1
                if match_index < 0:
                    # We ran out of matches to backtrack to.
                    return False
            match_index += 1

        return True


if __name__ == "__main__":
    TEST_CASES = [
        ("", "", True),
        ("a", "", False),
        ("", "a", False),
        ("", "a*", True),
        ("a", "a", True),
        ("a", "a*", True),
        ("aa", "a*", True),
        ("aa", "aa*", True),
        ("aa", "a*a", True),
        ("aa", "aa*a", True),
    ]

    for *case, expected in TEST_CASES:
        print("case", case)
        actual = Solution().isMatch(*case)
        if actual != expected:
            print(f"FAILURE! action: {actual} expected: {expected}")
