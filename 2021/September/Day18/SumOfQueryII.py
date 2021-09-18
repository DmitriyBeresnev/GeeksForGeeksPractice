

# GeeksForGeeks Practice. Problem of the Day. September. Day 18. Sum of Query II

'''


Sum of Query II
Medium Accuracy: 84.11% Submissions: 3244 Points: 4

You are given an array arr[] of n integers and q queries in an array queries[] of length 2*q containing l, r pair for all q queries. You need to compute the following sum over q queries.



Array is 1-Indexed.

Example 1:

Input: n = 4
arr = {1, 2, 3, 4}
q = 2
queries = {1, 4, 2, 3}
Output: 10 5
Explaination: In the first query we need sum
from 1 to 4 which is 1+2+3+4 = 10. In the
second query we need sum from 2 to 3 which is
2 + 3 = 5.

Your Task:
You do not need to read input or print anything. Your task is to complete the function querySum() which takes n, arr, q and queries as input parameters and returns the answer for all the queries.

Expected Time Complexity: O(n+q)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n, q ≤ 1000
1 ≤ arri ≤ 106
1 ≤ l ≤ r ≤ n

Company Tags
Amazon
Topic Tags
Mathematical



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


# my solution
class Solution:
    def querySum(self, n: int, arr: List[int], q: int, queries: List[int]):
        # code here
        def tot(arr: List[int], l: int, r: int):
            s = 0
            for i in range(l - 1, r):
                s = s + arr[i]
            return s

        res = []
        for i in range(q):
            res.append(tot(arr, queries[i * 2], queries[i * 2 + 1] ))
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
