#!/usr/bin/env python3

from typing import List, Tuple

def positive_minmax(nums: List[int]) -> Tuple[int, int]:
    positives = list(n for n in nums if n > 0)
    if not positives:
        return 0, 0
    return min(positives), max(positives)

def partition_positive(nums: List[int]) -> int:
    end = len(nums)
    for index in range(len(nums)):
        swap_index = end - 1
        while nums[index] <= 0 and index < swap_index:
            nums[index], nums[swap_index] = nums[swap_index], nums[index]
            end -= 1
            swap_index = end - 1
        if nums[index] <= 0:
            end = index
            break
    return end

def zero_out_of_range(nums: List[int], lowest: int, end: int):
    for index in range(end):
        if nums[index] - lowest >= end:
            nums[index] = 0

def first_missing(nums: List[int], end: int) -> int:
    missing = 1
    for index in range(0, end):
        if nums[index] != missing:
            break
        missing += 1
    return missing

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lowest, highest = positive_minmax(nums)
        if highest < 1:
            return 1

        end = len(nums)
        last_end = 0
        while end != last_end:
            last_end = end
            zero_out_of_range(nums, lowest, end)
            end = partition_positive(nums)
        print(nums, end)

        index = 0
        while index < end:
            swap_index = nums[index] - lowest
            while index < end and index != swap_index:
                if nums[index] == nums[swap_index]:
                    end -= 1
                    swap_index = end - 1
                print(nums)
                print("i", index)
                print("n", nums[index])
                print("l", lowest)
                print("e", end)
                print("s", swap_index)
                if index < end:
                    nums[index], nums[swap_index] = nums[swap_index], nums[index]
                    swap_index = nums[index] - lowest
            index += 1
        print(nums)

        return first_missing(nums, end)

TEST_CASES = (
    ([1,2,0], 3),
    ([1,3,-1,0], 2),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1),
    ([1], 2),
    ([1,2,3], 4),
    ([0], 1),
    ([], 1),
    ([-1,-2], 1),
    ([1000,-1], 1),
    ([1,1000], 2),
    ([-1,4,2,1,9,10], 3),
    ([3,1], 2),
    ([2147483647,100000,1,3,2,4,5,6,7,100001], 8),
    ([1,1], 2),
    ([1,3,3], 2),
    ([1,1,2,2,4], 3),
    ([1,2,2,1,3,1,0,4,0], 5),
)

for test_case, expected in TEST_CASES:
    actual = Solution().firstMissingPositive(test_case[:])
    assert actual == expected, f"{str(test_case)}\nactual:   {actual}\nexpected: {expected}"
