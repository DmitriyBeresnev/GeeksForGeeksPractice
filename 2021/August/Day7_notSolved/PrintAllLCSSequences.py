

# Print all LCS sequences

'''


Print all LCS sequences
Hard Accuracy: 58.53% Submissions: 1672 Points: 8

You are given two strings s and t. Now your task is to print all longest common sub-sequences in lexicographical order.

Example 1:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa

Example 2:

Input: s = aaa, t = a
Output: a

Your Task:
You do not need to read or print anything. Your task is to complete the function all_longest_common_subsequences() which takes string a and b as first and second parameter respectively and returns a list of strings which contains all possible longest common subsequences in lexicographical order.


Expected Time Complexity: O(n^4)
Expected Space Complexity: O(K * n) where K is a constant less than n.


Constraints:
1 <= Length of both strings <= 100

Topic Tags
Backtracking
Dynamic Programming



https://www.techiedelight.com/longest-common-subsequence-finding-lcs/

https://www.geeksforgeeks.org/printing-longest-common-subsequence-set-2-printing/

https://habr.com/ru/post/142825/

https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BE%D0%B1%D1%89%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C

https://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BE_%D0%BD%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%D0%B9_%D0%BE%D0%B1%D1%89%D0%B5%D0%B9_%D0%BF%D0%BE%D0%B4%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8

https://foxford.ru/wiki/informatika/naibolshaya-obschaya-podposledovatelnost

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
# Function to return all LCS of substrings `X[0…m-1]`, `Y[0…n-1]`
def LCS(X, Y, m, n, T):
    # if the end of either sequence is reached
    if m == 0 or n == 0:
        # create a list with one empty string and return
        return [""]

        # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:

        # ignore the last characters of `X` and `Y` and find all LCS of substring
        # `X[0…m-2]`, `Y[0…n-2]` and store it in a list
        lcs = LCS(X, Y, m - 1, n - 1, T)

        # append current character `X[m-1]` or `Y[n-1]`
        # to all LCS of substring `X[0…m-2]` and `Y[0…n-2]`
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (X[m - 1])

        return lcs

        # we reach here when the last character of `X` and `Y` don't match

        # if a top cell of the current cell has more value than the left cell,
        # then ignore the current character of string `X` and find all LCS of
        # substring `X[0…m-2]`, `Y[0…n-1]`
    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)

        # if a left cell of the current cell has more value than the top cell,
        # then ignore the current character of string `Y` and find all LCS of
        # substring `X[0…m-1]`, `Y[0…n-2]`
    if T[m][n - 1] > T[m - 1][n]:
        return LCS(X, Y, m, n - 1, T)

        # if the top cell has equal value to the left cell, then consider both characters

    top = LCS(X, Y, m - 1, n, T)
    left = LCS(X, Y, m, n - 1, T)

    # merge two lists and return
    return top + left


class Solution:
    def all_longest_common_subsequences(self, s, t):
        # Code here
        n = len(s)
        m = len(t)
        F = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    F[i][j] = F[i - 1][j - 1] + 1
                else:
                    F[i][j] = max(F[i - 1][j], F[i][j - 1])

        res = list(set(LCS(s, t, n, m, F)))
        return sorted(res)


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
