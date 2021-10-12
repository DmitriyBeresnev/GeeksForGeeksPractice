

# GeeksForGeeks Practice. Problem of the Day. October. Day 10. Valid Pair Sum

'''


Valid Pair Sum
Medium Accuracy: 30.49% Submissions: 7267 Points: 4

Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.

Example 1:

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two
possible pairs.

Example 2:

Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.

Your Task:
You don't need to read input or print anything. Complete the function ValidPair() which takes the array a[ ] and size of array N as input parameters and returns the count of such pairs.

Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
-104  ≤ a[i] ≤ 104

View Bookmarked Problems
Topic Tags
Arrays
Sorting
Searching
Greedy



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
    def binarySearch(self, arr: List[int], n: int, el: int) -> int:
        low = 0
        high = n-1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            v = arr[mid]
            if v == el:
                return mid
            if v > el:
                high = mid - 1
            else:
                low = mid + 1
        return mid

    def ValidPair(self, a: List[int], n: int) -> int:
        # Your code goes here
        res = 0
        sortedArr = sorted(a)
        for i in range(0, n):
            if sortedArr[i] > 0:
                j = self.binarySearch(sortedArr, i, -(sortedArr[i]-1))
                res += i - j
        return res

    def ValidPair2(self, a: List[int], n: int) -> int:
        # Your code goes here
        res = 0
        sortedArr = sorted(a)
        for i in range(0, n):
            if sortedArr[i] > 0:
                j = i-1
                while abs(sortedArr[j]) < sortedArr[i]:
                    j -= 1
                res += i - j - 1
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.ValidPair(a=[-4, 4, -5, 5, 3, -2, -3, -1, 2, 1], n=10)) #
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.ValidPair(a=[3, -2, 1], n=3)) #
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
