

# GeeksForGeeks Practice. Problem of the Day. October. Day 4. Maximum difference of zeros and ones in binary string

'''


Maximum difference of zeros and ones in binary string
Easy Accuracy: 51.77% Submissions: 11315 Points: 2

Given a binary string S consisting of 0s and 1s. The task is to find the maximum difference of the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a string.

Note: In the case of all 1s, the answer will be -1.

Example 1:

Input : S = "11000010001"
Output : 6
Explanatio: From index 2 to index 9,
there are 7 0s and 1 1s, so number
of 0s - number of 1s is 6.

Example 2:

Input: S = "111111"
Output: -1
Explanation: S contains 1s only

Your task:
You do not need to read any input or print anything. The task is to complete the function maxSubstring(), which takes a string as input and returns an integer.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1 ≤ |S| ≤ 105
S contains 0s and 1s only

Topic Tags
Dynamic Programming
Kadane
Strings



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
    def maxSubstring(self, S: str) -> int:
        # code here
        res = 0
        curSubstringCnt = 0
        for c in S:
            if c == "0":
                curSubstringCnt += 1
                res = max(res, curSubstringCnt)
            elif curSubstringCnt > 0:
                curSubstringCnt -= 1
        return res if res > 0 else -1


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
