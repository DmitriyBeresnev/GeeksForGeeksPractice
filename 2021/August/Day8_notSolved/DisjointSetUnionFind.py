

# Disjoint set (Union-Find)

'''


Disjoint set (Union-Find)
Easy Accuracy: 38.83% Submissions: 3326 Points: 2

Given an array A[] that stores all number from 1 to N (both inclusive and sorted) and K queries.

The task is to do the following operations on array elements :

1. UNION X Z : Perform union of X and Z i.e. parent of Z will become the parent of X.
2. FIND X: Find the parent of X and print it.

Note: Initially all are the parent of themselves.

Input:
N = 5, K = 4
queries[] = {{find 4},
             {find 1},
             {unionSet 3 1},
             {find 3}}
Output:
4 1 1
Explanation:
1. The parent of 4 is 4. Hence the output is 4.
2. The parent of 1 is 1. Hence the output is 1.
3. After performing unionSet 3 1, parent of 3 becomes 1,
   since, parent of 1 is currently 1 itself.
4. The parent of 3 is now 1. Hence, the output is 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the functions- find() which takes an array A[] and an integer X as an input parameter and return the parent of X and the function unionSet() which takes an array A[] and two integers X and Z and performs the union of X and Z.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N, K <= 100

Company Tags
Samsung
Topic Tags
Union-find
Related Interview Experiences
Samsung bangalore sri b interview experience




https://www.geeksforgeeks.org/union-find/

https://cp-algorithms.com/data_structures/disjoint_set_union.html

https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/

https://en.wikipedia.org/wiki/Disjoint-set_data_structure

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

# function should return parent of x
def find(A: List[int], X: int) -> int:
    # Code here
    pass


# function shouldn't return or print anything
def unionSet(A: List[int], X: int, Z: int) -> None:
    # Code here
    pass


from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        parent[x] = y

    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):

        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print
    "Graph contains cycle"
else:
    print
    "Graph does not contain cycle "


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
