

# GeeksForGeeks Practice. Problem of the Day. October. Day 1. Check for BST

'''


Check for BST
Easy Accuracy: 21.58% Submissions: 100k+ Points: 2

Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input:
   2
 /    \
1      3
Output: 1
Explanation:
The left subtree of root node contains node
with key lesser than the root node’s key and
the right subtree of root node contains node
with key greater than the root node’s key.
Hence, the tree is a BST.

Example 2:

Input:
  2
   \
    7
     \
      6
       \
        5
         \
          9
           \
            2
             \
              6
Output: 0
Explanation:
Since the node with value 7 has right subtree
nodes with keys less than 7, this is not a BST.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isBST() which takes the root of the tree as a parameter and returns true if the given binary tree is BST, else returns false.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
0 <= Number of edges <= 100000

Company Tags
Accolite
Adobe
Amazon
Boomerang Commerce
FactSet
Flipkart
Goldman Sachs
GreyOrange
Hike
Linkedin
MakeMyTrip
MAQ Software
Microsoft
Ola Cabs
OYO Rooms
Qualcomm
Samsung
Snapdeal
VMWare
Walmart
Wooker
Topic Tags
Binary Search Tree
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
Must Do Coding Questions
Geeks Classes - Live Session
Competitive Programming - Live
First Step to Data Structures and Algorithms
Placement Guide 2021-2022
Related Interview Experiences
Accolite interview experience set 7 on campus
Vmware interview experience set 4 campus
Walmart labs interview experience set 5 on campus
Qualcomm interview experience set 12 campus
Makemytrip interview experience set 8 on campus
Samsung research institute bangalore srib intern



A program to check if a binary tree is BST or not
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/


'''


import math
import time
import collections
from typing import List, Optional
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
    def __init__(self, key: int):
        self.data = key
        self.left = None
        self.right = None


# my solution
class Solution:
    def isBstCheck(self, root: Node, left: Optional[Node], right: Optional[Node]) -> bool:
        # Base condition
        if root is None:
            return True
        # if left node exist then check it has correct data or not i.e. left node's data
        # should be less than root's data
        if left is not None:
            if root.left.data > left.data:
                return False
        # if right node exist then check it has correct data or not i.e. right node's data
        # should be greater than root's data
        if right is not None:
            if root.right.data <= right.data:
                return False
        # check recursively for every node.
        return self.isBstCheck(root.left, left, root) and self.isBstCheck(root.right, root, right)

    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root: Node) -> bool:
        # code here
        return self.isBstCheck(root, None, None)


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
