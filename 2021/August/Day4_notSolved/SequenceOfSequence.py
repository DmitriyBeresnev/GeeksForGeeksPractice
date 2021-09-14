

# Sequence of Sequence

'''


Sequence of Sequence
Easy Accuracy: 72.82% Submissions: 1230 Points: 2

Given two integers m & n, find the number of possible sequences of length n such that each of the next element is greater than or equal to twice of the previous element but less than or equal to m.


Example 1:

Input: m = 10, n = 4
Output: 4
Explaination: There should be n elements and
value of last element should be at-most m.
The sequences are {1, 2, 4, 8}, {1, 2, 4, 9},
{1, 2, 4, 10}, {1, 2, 5, 10}.


Example 2:

Input: m = 5, n = 2
Output: 6
Explaination: The sequences are {1, 2},
{1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}.


Your Task:
You do not need to read input or print anything. Your task is to complete the function numberSequence() which takes the number m and n as input parameters and returns the number of sequences.


Expected Time Complexity: O(m*n)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ m, n ≤ 100

Topic Tags
Divide and Conquer



https://www.geeksforgeeks.org/sequences-given-length-every-element-equal-twice-previous/

'''


import math
import time
import collections
from typing import List
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from bisect import bisect, bisect_left

from collections import Counter, defaultdict
import sys



# my solution (found in the inet)
class Solution:
    def numberSequence(self, m, n):
        # code here
        # A special sequence cannot exist if length
        # n is more than the maximum value m.
        if m < n:
            return 0

        # If n is 0, found an empty special sequence
        if n == 0:
            return 1

        # There can be two possibilities : (1) Reduce
        # last element value (2) Consider last element
        # as m and reduce number of terms
        res = (self.numberSequence(m - 1, n) +
               self.numberSequence(m // 2, n - 1))
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.maxBalls(N = 5, M = 5, a = [1, 4, 5, 6, 8], b = [2, 3, 4, 6, 9])) #
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.maxSubArray(nums = [1])) #
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.maxSubArray(nums = [5,4,-1,7,8])) #
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.maxProfit(prices = [2,1,2,1,0,1,2])) #
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.maxProfit(prices = [3,3,5,0,0,3,1,4])) #
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
