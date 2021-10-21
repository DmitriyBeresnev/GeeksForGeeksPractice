

# GeeksForGeeks Practice. Problem of the Day. October. Day 22. Top View of Binary Tree

'''


Top View of Binary Tree
Medium Accuracy: 32.3% Submissions: 99038 Points: 4

Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3

Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100

Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ Node Data ≤ 105


Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

View Bookmarked Problems
Company Tags
Walmart
Ola Cabs
Paytm
Topic Tags
Binary Search Tree
Tree
Related Courses
DSA-Self Paced with Doubt Assistance
Data Structures and Algorithms
Placement 100
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Competitive Programming - Live
DSA Live for Working Professionals
First Step to Data Structures and Algorithms
Related Interview Experiences
Paytm interview experience set 12 1 5 years experienced
Walmart labs interview experience set 5 on campus



https://www.techiedelight.com/print-top-view-binary-tree/

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
    def __init__(self, val: int):
        self.left = None
        self.data = val
        self.right = None


# my solution
class Solution:
    # Recursive function to perform preorder traversal on the tree and fill the dictionary.
    # Here, the node has `dist` horizontal distance from the tree's root,
    # and the level represents the node's level.
    def printTop(self, root: Node, dist: int, level: int, d: dict):

        # base case: empty tree
        if root is None:
            return

        # if the current level is less than the maximum level seen so far
        # for the same horizontal distance, or if the horizontal distance
        # is seen for the first time, update the dictionary
        if dist not in d or level < d[dist][1]:
            # update value and level for current distance
            d[dist] = (root.data, level)

        # recur for the left subtree by decreasing horizontal distance and
        # increasing level by 1
        self.printTop(root.left, dist - 1, level + 1, d)

        # recur for the right subtree by increasing both level and
        # horizontal distance by 1
        self.printTop(root.right, dist + 1, level + 1, d)

    # Function to return a list of nodes visible from the top view from left to right in Binary Tree.
    def topView(self, root: Node) -> List[int]:
        # code here
        # create a dictionary where
        # key —> relative horizontal distance of the node from the root node, and
        # value —> pair containing the node's value and its level
        d = {}

        # perform preorder traversal on the tree and fill the dictionary
        self.printTop(root, 0, 0, d)

        res = list()
        # traverse the dictionary in sorted order of keys and print the top view
        for key in sorted(d.keys()):
            res.append(d.get(key)[0])
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
