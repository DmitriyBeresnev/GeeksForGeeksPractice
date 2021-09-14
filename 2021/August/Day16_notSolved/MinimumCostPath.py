

# Minimum Cost Path

'''


Minimum Cost Path
Hard Accuracy: 50.09% Submissions: 12076 Points: 8

Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).

Note: It is assumed that negative cost cycles do not exist in the input matrix.


Example 1:

Input: grid = {{9,4,9,9},{6,7,6,4},
{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.

Example 2:

Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7
The minimum cost is- 4 + 3 + 7 = 14.



Your Task:
You don't need to read or print anything. Your task is to complete the function minimumCostPath() which takes grid as input parameter and returns the minimum cost to react at bottom right cell from top left cell.


Expected Time Compelxity: O(n2*log(n))
Expected Auxiliary Space: O(n2)


Constraints:
1 ≤ n ≤ 500
1 ≤ cost of cells ≤ 1000

Company Tags
Goldman Sachs
MakeMyTrip
Samsung
Amazon
Microsoft
Topic Tags
Dynamic Programming
Graph
Greedy
Related Courses
Must Do Interview Preparation
DSA-Self Paced with Doubt Assistance
Data Structures and Algorithms
Amazon SDE Test Series
Placement 100
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Microsoft SDE Test Series
Live Classes on Data Structures & Algorithms - USA
Competitive Programming - Live
Geeks Classes - Live Session
Must Do Coding Questions
First Step to Data Structures and Algorithms
Related Interview Experiences
Makemytrip interview experience set 2 campus
Samsung interview experience through co cubes 2019


i rewrite this solution
https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/

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


class Cell:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.distance = 0

    @staticmethod
    def compareCells(a, b) -> bool:
        if a.distance == b.distance:
            if a.x != b.x:
                return a.x < b.x
            else:
                return a.y < b.y
        return a.distance < b.distance


# my solution (found in the inet)
class Solution:
    def isInsideGrid(self, i: int, j: int, n: int, m: int) -> bool:
        return i >= 0 and i < n and j >= 0 and j < m

    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    def minimumCostPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # initializing distance array by MAX Integer
        distanceMatrix = [[sys.maxsize] * m for _ in range(n)]
        # direction arrays for simplification of getting neighbour
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        # initialize distance of(0, 0) with its grid value
        distanceMatrix[0][0] = grid[0][0]
        #
        uniqueListOfCells = set()
        # loop for standard dijkstra's algorithm
        while(len(uniqueListOfCells) > 0):
            #cell = uniqueListOfCells.
            uniqueListOfCells.remove(cell)


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
