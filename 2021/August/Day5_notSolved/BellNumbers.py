

# Bell Numbers

'''

Bell Numbers
Easy Accuracy: 42.52% Submissions: 1326 Points: 2

Given a set of n elements, find number of ways of partitioning it.



Example 1:

Input:
N = 2
Output: 2
Explanation:
Let the set be
{1, 2}:
{ {1}, {2} } { {1, 2} }



Example 2:

Input:
N = 3
Output: 5


Your Task:
You don't need to read input or print anything. Your task is to complete the function bellNumber() which takes the integer N as input parameters and returns the number of ways of partitioning n elements. Since the value can be quite large print the value modulo 109+7.

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(N^2)



Constraints:

1 ≤ N ≤ 1000

Topic Tags
Dynamic Programming


https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/

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
    def bellNumber(self, N):
        n = N
        # code here
        bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
        bell[0][0] = 1
        for i in range(1, n + 1):

            # Explicitly fill for j = 0
            bell[i][0] = bell[i - 1][i - 1]

            # Fill for remaining values of j
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

        return bell[n][0]


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
