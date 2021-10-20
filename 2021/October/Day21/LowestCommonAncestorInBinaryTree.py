

# GeeksForGeeks Practice. Problem of the Day. October. Day 21. Lowest Common Ancestor in a Binary Tree

'''


Lowest Common Ancestor in a Binary Tree
Medium Accuracy: 39.75% Submissions: 82169 Points: 4

Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them is present.

Example 1:

Input:
n1 = 2 , n2 =  3
     1
   /  \
  2    3
Output: 1
Explanation:
LCA of 2 and 3 is 1.

Example 2:

Input:
n1 = 3 , n2 = 4
         5
        /
       2
     /  \
    3    4
Output: 2
Explanation:
LCA of 3 and 4 is 2.

Your Task:
You don't have to read input or print anything. Your task is to complete the function lca() that takes nodes, n1, and n2 as parameters and returns LCA node as output. Otherwise return a node with value -1 if both n1 and n2 is not present in the tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105

View Bookmarked Problems
Company Tags
Topic Tags
Tree
Related Courses
Must Do Interview Preparation
DSA-Self Paced with Doubt Assistance
Data Structures and Algorithms
Amazon SDE Test Series
Placement 100
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Microsoft SDE Test Series
Google Test Series
Must Do Coding Questions
Competitive Programming - Live
DSA Live for Working Professionals
Placement Guide 2021-2022
First Step to Data Structures and Algorithms
Related Interview Experiences
Accolite interview experience set 11 on campus
American express interview experience set 2
Flipkart interview experience set 17 for sde ii



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


class Node:
    def __init__(self, value: int):
        self.left = None
        self.data = value
        self.right = None


# my solution
class Solution:

    # Finds the path from root node to given root of the tree.
    # Stores the path in a stack path[], returns true if path
    # exists otherwise false
    def findPath(self, root: Node, path: list, valuesPath: list, k: int) -> bool:
        # Baes Case
        if root is None:
            return False
        # Store this node is path stack. The node will be removed if not in path from root to k
        path.append(root)
        #
        valuesPath.append(root.data)
        # See if the k is same as root's data
        if root.data == k:
            return True
        # Check if k is found in left or right sub-tree
        if ((root.left is not None and self.findPath(root.left, path, valuesPath, k)) or
                (root.right is not None and self.findPath(root.right, path, valuesPath, k))):
            return True
        # If not present in subtree rooted with root, remove root from path and return False
        path.pop()
        valuesPath.pop()
        return False

    # Function to return the lowest common ancestor in a Binary Tree.
    # Returns LCA if node n1 , n2 are present in the given binary tre otherwise return -1
    def lca(self, root: Node, n1: int, n2: int) -> Node:
        # Code here
        if root is None:
            return -1
        # To store paths to n1 and n2 from the root
        path1 = []
        path2 = []
        path1v = []
        path2v = []
        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        if (not self.findPath(root, path1, path1v, n1) or not self.findPath(root, path2, path2v, n2)):
            return -1
        # Compare the paths to get the first different value
        i = 0
        while (i < len(path1v) and i < len(path2v)):
            if path1v[i] != path2v[i]:
                break
            i += 1
        return path1[i - 1]


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
