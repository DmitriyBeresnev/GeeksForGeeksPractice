

# Maximum XOR subarray

'''


Maximum XOR subarray
Medium Accuracy: 47.34% Submissions: 13147 Points: 4

Given an array arr[] of size, N. Find the subarray with maximum XOR. A subarray is a contiguous part of the array.


Example 1:

Input:
N = 4
arr[] = {1,2,3,4}
Output: 7
Explanation:
The subarray {3,4} has maximum xor
value equal to 7.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSubarrayXOR() which takes the array arr[], its size N as input parameters and returns the maximum xor of any subarray.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)



Constraints:
1 <= N <= 105
1 <= arr[i] <= 105

Company Tags
Microsoft
Topic Tags
Trie
Related Courses
Must Do Interview Preparation
Microsoft SDE Test Series
Must Do Coding Questions



https://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/

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
"""structure of Trie Node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # left node for 0
        self.right = None  # right node for 1


""" class for implementing Trie """
class Trie:
    def __init__(self):
        self.root = Node(0)

    """insert pre_xor to trie with given root"""
    def insert(self, pre_xor):

        self.temp = self.root

        """start from msb, insert all bits of pre_xor
        into the Trie"""
        for i in range(31, -1, -1):

            """Find current bit in prefix sum"""
            val = pre_xor & (1 << i)

            if val:
                """create new node if needed"""
                if not self.temp.right:
                    self.temp.right = Node(0)
                self.temp = self.temp.right

            if not val:
                """create new node if needed"""
                if not self.temp.left:
                    self.temp.left = Node(0)
                self.temp = self.temp.left

        """store value at leaf node"""
        self.temp.data = pre_xor

    """find the maximum xor ending with last number
        in prefix XOR and return the XOR of this"""
    def query(self, xor):

        self.temp = self.root

        for i in range(31, -1, -1):

            """find the current bit in prefix xor"""
            val = xor & (1 << i)

            """Traverse the trie, first look for opposite bit
                and then look for same bit"""
            if val:
                if self.temp.left:
                    self.temp = self.temp.left
                elif self.temp.right:
                    self.temp = self.temp.right
            else:
                if self.temp.right:
                    self.temp = self.temp.right
                elif self.temp.left:
                    self.temp = self.temp.left

        return xor ^ self.temp.data


class Solution:
    """returns maximum XOR value of subarray"""
    def maxSubArrayXOR(self, n, Arr):

        trie = Trie()
        """insert 0 in the trie"""
        trie.insert(0)

        """initialize result and pre_xor"""
        result = -float('inf')
        pre_xor = 0

        """traverse all input array element"""
        for i in range(n):
            """update current prefix xor and insert it into Trie"""
            pre_xor = pre_xor ^ Arr[i]
            trie.insert(pre_xor)

            """Query for current prefix xor in Trie and update result"""
            result = max(result, trie.query(pre_xor))

        return result


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
