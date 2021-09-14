

# Lucky alive person in a circle

'''


Lucky alive person in a circle
Medium Accuracy: 66.82% Submissions: 812 Points: 4

Given N people standing in a circle where 1st is having a sword, find the luckiest person in the circle, if, from 1st soldier who is having a sword each has to kill the next soldier and handover the sword to next soldier, in turn, the soldier will kill the adjacent soldier and handover the sword to next soldier such that one soldier remains in this war who is not killed by anyone.


Example 1:

Input:
N = 5
Output:
3
Explanation:
In first go 1 3 5 (remains)
as 2 and 4 killed by 1 and 3.
In second go 3 will remain
as 5 killed 1 and 3rd killed 5
hence, 3 remains alive.

Example 2:

Input:
N = 10
Output:
5
Explanation:
In first 1 3 5 7 9
remains as 2 4 6 8 10
were killed by 1 3 5 7
and 9. In second 1 5 9
are left as 1 kills 3
and  5 kill the 7th
soldier.In third 5th
soldiers remain alive as
9 kills the 1st soldier and
5 kill the 9th soldier.


Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes an integer N as input parameter and returns the output as the soldier who was lucky in the game.


Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)


Constraints:
1<=N<=108

Topic Tags
Bit Magic
Circular linked list
Circular-linked-list



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
    def find(self, N: int) -> int:
        # code here
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
