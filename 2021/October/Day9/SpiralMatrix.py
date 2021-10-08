

# GeeksForGeeks Practice. Problem of the Day. October. Day 9. Spiral Matrix

'''


Spiral Matrix
Medium Accuracy: 32.65% Submissions: 6082 Points: 4

Given a matrix of size N x M. You have to find the Kth element which will obtain while traversing the matrix spirally starting from the top-left corner of the matrix.

Example 1:

Input:
N = 3, M = 3, K = 4
A[] = {{1, 2, 3},
       {4, 5, 6},
       {7, 8, 9}}
Output:
6
Explanation: Spiral traversal of matrix:
{1, 2, 3, 6, 9, 8, 7, 4, 5}. Fourth element
is 6.

Example 2:

Input:
N = 2, M = 2, K = 2
A[] = {{1, 2},
       {3, 4}}
Output:
2
Explanation: Spiral traversal of matrix:
{1, 2, 4, 3}. Second element is 2.

Your Task:
You don't need to read input or print anything. Complete the function findK() which takes the matrix A[ ][ ], number of rows N, number of columns M, and integer K as input parameters and returns the Kth element in the spiral traversal of the matrix.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ K ≤ N*M ≤ 106

View Bookmarked Problems
Topic Tags
Matrix
Constructive algo



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
# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        totalNumsCount = n * m
        startRowIndex = 0
        startColIndex = 0
        num = 0
        res = list()
        while num != totalNumsCount:
            for j in range(startColIndex, m):
                res.append(matrix[startRowIndex][j])
                num += 1
            if num == totalNumsCount:
                return res
            startRowIndex += 1
            for i in range(startRowIndex, n):
                res.append(matrix[i][m - 1])
                num += 1
            if num == totalNumsCount:
                return res
            m -= 1
            for j in range(m - 1, startColIndex - 1, -1):
                res.append(matrix[n - 1][j])
                num += 1
            if num == totalNumsCount:
                return res
            startColIndex += 1
            n -= 1
            if num == totalNumsCount:
                return res
            for i in range(n - 1, startRowIndex - 1, -1):
                res.append(matrix[i][startColIndex - 1])
                num += 1
        return res

    def findK(self, a: List[List[int]], n: int, m: int, k: int) -> int:
        # Your code goes here
        matrix = a
        totalNumsCount = n * m
        startRowIndex = 0
        startColIndex = 0
        num = 0
        while num != totalNumsCount:
            for j in range(startColIndex, m):
                num += 1
                if num == k:
                    return matrix[startRowIndex][j]
            startRowIndex += 1
            for i in range(startRowIndex, n):
                num += 1
                if num == k:
                    return matrix[i][m - 1]
            m -= 1
            for j in range(m - 1, startColIndex - 1, -1):
                num += 1
                if num == k:
                    return matrix[n - 1][j]
            startColIndex += 1
            n -= 1
            for i in range(n - 1, startRowIndex - 1, -1):
                num += 1
                if num == k:
                    return matrix[i][startColIndex - 1]


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
