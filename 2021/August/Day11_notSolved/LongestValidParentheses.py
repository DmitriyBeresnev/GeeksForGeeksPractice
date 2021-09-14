

# Longest valid Parentheses

'''


Longest valid Parentheses
Hard Accuracy: 43.77% Submissions: 9181 Points: 8

Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

Example 1:

Input: S = ((()
Output: 2
Explaination: The longest valid
parenthesis substring is "()".

Example 2:

Input: S = )()())
Output: 4
Explaination: The longest valid
parenthesis substring is "()()".

Your Task:
You do not need to read input or print anything. Your task is to complete the function maxLength() which takes string S as input parameter and returns the length of the maximum valid parenthesis substring.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1 ≤ |S| ≤ 105

Company Tags
Google
Microsoft
Topic Tags
Stack
Strings
Dynamic Programming
Related Courses
Must Do Interview Preparation
Microsoft SDE Test Series
Google Test Series
Must Do Coding Questions



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
    def maxLength(self, S: str) -> int:
        # code here
        stack = list()
        symbolsList = list(S)
        maxLength = 0
        curLength = 0
        isLastActionStackPop = False
        for i, symbol in enumerate(symbolsList):
            if len(stack) > 0:
                if stack[-1] == "(" and symbol == ")":
                    stack.pop()
                    isLastActionStackPop = True
                    if isLastActionStackPop:
                        curLength += 2
                        maxLength = max(maxLength, curLength)
                    else:
                        maxLength = max(maxLength, curLength)
                        curLength = 0
                        isLastActionStackPop = False
                else:
                    stack.append(symbol)
                    isLastActionStackPop = False
            else:
                stack.append(symbol)
                isLastActionStackPop = False
        return maxLength


def findMaxLen(string):
    n = len(string)

    # Create a stack and push -1
    # as initial index to it.
    stk = []
    stk.append(-1)

    # Initialize result
    result = 0

    # Traverse all characters of given string
    for i in xrange(n):

        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)

        # If closing bracket, i.e., str[i] = ')'
        else:

            # Pop the previous opening bracket's index
            if len(stk) != 0:
                stk.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stk) != 0:
                result = max(result,
                             i - stk[len(stk) - 1])

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stk.append(i)

    return result


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.maxLength(S = '((()')) #
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
