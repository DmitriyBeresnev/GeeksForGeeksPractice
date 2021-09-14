

# Minimum steps to make product equal to one

'''


Minimum steps to make product equal to one
Easy Accuracy: 38.33% Submissions: 5134 Points: 2

Given an array arr[] containing N integers. In one step, any element of the array can either be increased or decreased by one. Find minimum steps required such that the product of the array elements becomes 1.



Example 1:

Input:
N = 3
arr[] = {-2, 4, 0}
Output:
5
Explanation:
We can change -2 to -1, 0 to -1 and 4 to 1.
So, a total of 5 steps are required
to update the elements such that
the product of the final array is 1.

Example 2:

Input:
N = 3
arr[] = {-1, 1, -1}
Output :
0
Explanation:
Product of the array is already 1.
So, we don't need to change anything.


Your Task:
You don't need to read input or print anything. Your task is to complete the function makeProductOne() which takes an integer N and an array arr of size N as input and returns the minimum steps required.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 105
-103 ≤ arr[i] ≤ 103

Company Tags
Amazon
Microsoft
Topic Tags
Arrays
Mathematical
Related Interview Experiences
Amazon interview experience 6 months intern for sde 1 on campus




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
    def makeProductOne(self, arr: List[int], N: int) -> int:
        # code here
        minSteps = 0
        totalProd = 1
        isZerosExist = False
        for i in range(0, N):
            if arr[i] != -1 and arr[i] != 1:
                minSteps += abs(abs(arr[i]) - 1)
            if arr[i] < 0:
                totalProd *= -1
            if arr[i] == 0:
                isZerosExist = True
        if totalProd == -1 and not isZerosExist:
            minSteps += 2
        return minSteps


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
