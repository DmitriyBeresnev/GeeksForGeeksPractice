

# GeeksForGeeks Practice. Problem of the Day. September. Day 25. Largest subarray with 0 sum

'''


Largest subarray with 0 sum
Easy Accuracy: 46.94% Submissions: 71151 Points: 2

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i

Company Tags
Amazon
MakeMyTrip
Microsoft
Topic Tags
Arrays
Hash
Related Courses
Amazon SDE Test Series
Microsoft SDE Test Series
Related Interview Experiences
Makemytrip interview experience set 8 on campus



1)Concept = > The main intution behind this is that if let suppose we are at some position ith ok. and let suppose after taking some steps kth step we reach at (i+k) position and there we check our value and if at that position the value which is at the ith position and value which we check at  (i+k)th position is same it means the element between i and i+k has sum =  0 because that is the only reason such that after takin some step there is no change in value right and we know if we add zero(0) to any number we have no change in that number and in that case length is equal to the (i+k - i) means where we are now and where we have that same value at ith  position and to check that is the value at ith position is repeated or not we use hashmaps

2)The second thing is also same as that but little bit tricky here if at some position we get the sum = 0 we simply find its length by (i-1) here i is the index where we are at right now .

3)Simply create a ans variable to store maximum length and update it with the maximum one .

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
    def maxLen(self, n: int, arr: List[int]) -> int:
        # Code here
        if n == 0:
            return 0
        prefixSumMap = dict()
        prefixSum = 0
        res = 0
        for i in range(0, n):
            prefixSum += arr[i]
            if prefixSum == 0:
                res = i + 1
            elif prefixSum in prefixSumMap:
                pos = prefixSumMap.get(prefixSum)
                if pos is not None:
                    res = max(res, i - pos)
            else:
                prefixSumMap.update({prefixSum: i})
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
