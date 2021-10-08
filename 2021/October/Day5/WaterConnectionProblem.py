

# GeeksForGeeks Practice. Problem of the Day. October. Day 5. Water Connection Problem

'''


Water Connection Problem
Medium Accuracy: 51.6% Submissions: 4600 Points: 4

Every house in the colony has at most one pipe going into it and at most one pipe going out of it. Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.

Given two integers n and p denoting the number of houses and the number of pipes. The connections of pipe among the houses contain three input values: ai, bi, di denoting the pipe of diameter di from house ai to house bi. Find the efficient way for the construction of the network of pipes.

The output will contain the number of pairs of tanks and taps t installed in first line and the next t lines contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.


Example 1:

Input:
n = 9, p = 6
a[] = {7,5,4,2,9,3}
b[] = {4,9,6,8,7,1}
d[] = {98,72,10,22,17,66}
Output:
3
2 8 22
3 1 66
5 6 10
Explanation:
Connected components are
3->1, 5->9->7->4->6 and 2->8.
Therefore, our answer is 3
followed by 2 8 22, 3 1 66, 5 6 10.



Your Task:
You don't need to read input or print anything. Your task is to complete the function solve() which takes an integer n(the number of houses), p(the number of pipes),the array a[] , b[] and d[] (where d[i] denoting the diameter of the ith pipe from the house a[i] to house b[i]) as input parameter and returns the array of pairs of tanks and taps installed i.e ith element of the array contains three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.



Expected Time Complexity: O(n+p)
Expected Auxiliary Space: O(n+p)



Constraints:
1<=n<=20
1<=p<=50
1<=a[i],b[i]<=20
1<=d[i]<=100

Topic Tags
DFS
Graph
Greedy



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
    def printAdjMatrix(self, adjMatrix: List[List[int]], size: int) -> None:
        for i in range(size):
            print(adjMatrix[i])

    def solve(self, n: int, p: int, a: List[int], b: List[int], d: List[int]) -> List[List[int]]:
        # code here
        adjMatrix = [[0] * n for _ in range(n)]
        for i, pipeDiameter in enumerate(d):
            adjMatrix[a[i]-1][b[i]-1] = pipeDiameter
        self.printAdjMatrix(adjMatrix, n)


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.solve(n=9, p=6, a=[7,5,4,2,9,3], b=[4,9,6,8,7,1], d=[98,72,10,22,17,66])) #
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
