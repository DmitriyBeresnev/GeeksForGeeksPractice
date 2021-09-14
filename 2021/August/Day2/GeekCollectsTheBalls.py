

# Geek collects the balls

'''


Geek collects the balls
Medium Accuracy: 46.98% Submissions: 3201 Points: 4

There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The balls in first road are given in an array a and balls in the second road in an array b. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
Geek can change the road only at a point of intersection ie- a point where buckets have the same number of balls on two roads. Help Geek collect the maximum number of balls.



Example 1:

Input:
N = 5, M = 5
a[] = {1, 4, 5, 6, 8}
b[] = {2, 3, 4, 6, 9}
Output: 29
Explanation: The optimal way to get the
maximum number of balls is to start from
road 2. Get 2+3. Then switch at intersection
point 4. Get 4+5+6. Then switch at intersection
point 6. Get 9. Total = 2+3+4+5+6+9 = 29.

Example 2:

Input:
N = 3, M = 3
a[] = {1, 2, 3}
b[] = {4, 5, 6}
Output: 15




Your Task:
You do not need to read input or print anything. Your task is to complete the function maxBalls() which takes N, M, a[] and b[] as input parameters and returns the maximum number of balls that can be collected.



Expected Time Complexity: O(N+M)
Expected Auxililary Space: O(1)



Constraints:
1 ≤ N, M ≤ 103
1 ≤ a[i], b[i] ≤ 106

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


# my solution
class Solution:
    def maxBalls(self, N, M, a, b):
        # code here
        first = 0
        second = 0
        res = 0
        i = 0
        j = 0
        while(i < N and j < M):
            if a[i] < b[j]:
                first += a[i]
                i += 1
            elif a[i] > b[j]:
                second += b[j]
                j += 1
            else:
                res += max(first, second) + a[i]
                first = 0
                second = 0
                temp = a[i]
                i += 1
                temp = b[j]
                j += 1
                while(i < N and a[i] == temp):
                    res += a[i]
                    i += 1
                while (j < M and b[j] == temp):
                    res += b[j]
                    j += 1
        while(i < N):
            first += a[i]
            i += 1
        while(j < M):
            second += b[j]
            j += 1
        res += max(first, second)
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
