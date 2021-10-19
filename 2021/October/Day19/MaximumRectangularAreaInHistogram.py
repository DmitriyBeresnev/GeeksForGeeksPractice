

# GeeksForGeeks Practice. Problem of the Day. October. Day 19. Maximum Rectangular Area in a Histogram

'''


Maximum Rectangular Area in a Histogram
Medium Accuracy: 47.42% Submissions: 42605 Points: 4

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be N bars height of each bar will be given by the array arr.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation:


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram
will be 8  and there will be 2 consecutive
histogram. And hence the area of the
histogram will be 8x2 = 16.

Your Task:
The task is to complete the function getMaxArea() which takes the array arr[] and its size N as inputs and finds the largest rectangular area possible and returns the answer.

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 1012

View Bookmarked Problems
Company Tags
Microsoft
Google
Topic Tags
Stack
Related Courses
Must Do Interview Preparation
DSA-Self Paced with Doubt Assistance
Data Structures and Algorithms
Placement 100
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Microsoft SDE Test Series
Google Test Series
Must Do Coding Questions
Competitive Programming - Live
DSA Live for Working Professionals
Placement Guide 2021-2022
First Step to Data Structures and Algorithms
Related Interview Experiences
One97 interview experience set 3 backendnode js developer



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
    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram: List[int]) -> int:
        # code here
        nBars = len(histogram)
        indecesStack = []
        res = 0
        for i in range(0, nBars+1):
            while indecesStack and (i == nBars or histogram[i] <= histogram[indecesStack[-1]]):
                height = histogram[indecesStack[-1]]
                indecesStack.pop()
                if len(indecesStack) == 0:
                    width = i
                else:
                    width = i - indecesStack[-1] - 1
                res = max(res, width * height)
            indecesStack.append(i)
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.getMaxArea([6,2,5,4,5,1,6])) # 12
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.getMaxArea([7, 2, 8, 9, 1, 3, 6, 5])) # 16
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.getMaxArea([1, 2, 3, 4, 5])) # 9
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
