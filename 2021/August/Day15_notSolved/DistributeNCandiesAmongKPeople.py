

# Distribute N candies among K people

'''


Distribute N candies among K people
Medium Accuracy: 54.82% Submissions: 2430 Points: 4

Given N candies and K people. In the first turn, the first person gets 1 candy, the second gets 2 candies, and so on till K people. In the next turn, the first person gets K+1 candies, the second person gets K+2 candies and so on. If the number of candies is less than the required number of candies at every turn, then the person receives the remaining number of candies. Find the total number of candies every person has at the end.



Example 1:

Input:
N = 7, K = 4
Output:
1 2 3 1
Explanation:
At the first turn, the fourth person
has to be given 4 candies, but there is
only 1 left, hence he takes only one.

Example 2:

Input:
N = 10, K = 3
Output :
5 2 3
Explanation:
At the second turn first one receives
4 and then we have no more candies left.


Your Task:
You don't need to read input or print anything. Your task is to complete the function distributeCandies() which takes 2 integers N and K as input and returns a list, where the ith integer denotes the number of candies the ith person gets.


Expected Time Complexity: O(logN+K)
Expected Auxiliary Space: O(K)


Constraints:
1 ≤ N ≤ 108
1 ≤ K ≤ 100

Company Tags
Microsoft
Topic Tags
Arrays
Binary Search
Mathematical
Related Interview Experiences
Microsoft internship interview experience 4



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
    pass


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
