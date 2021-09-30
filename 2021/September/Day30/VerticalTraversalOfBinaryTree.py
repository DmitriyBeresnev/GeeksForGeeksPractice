

# GeeksForGeeks Practice. Problem of the Day. September. Day 30. Vertical Traversal of Binary Tree

'''


Vertical Traversal of Binary Tree
Medium Accuracy: 32.45% Submissions: 100k+ Points: 4

Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Example 1:

Input:
           1
         /   \
       2       3
     /   \   /   \
   4      5 6      7
              \      \
               8      9
Output:
4 2 1 5 6 3 8 7 9
Explanation:

Example 2:

Input:
       1
    /    \
   2       3
 /    \      \
4      5      6
Output: 4 2 1 5 3 6

Your Task:
You don't need to read input or print anything. Your task is to complete the function verticalOrder() which takes the root node as input parameter and returns an array containing the vertical order traversal of the tree from the leftmost to the rightmost level. If 2 nodes lie in the same vertical level, they should be printed in the order they appear in the level order traversal of the tree.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 3*104

Company Tags
Accolite
Amazon
BrowserStack
Dell
Flipkart
Grofers
MakeMyTrip
Netskope
Walmart
Microsoft
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
Must Do Coding Questions
Geeks Classes - Live Session
Competitive Programming - Live
First Step to Data Structures and Algorithms
Related Interview Experiences
Amazon interview experience set 349 sde
Makemytrip interview experience set 4



Print a Binary Tree in Vertical Order | Set 3 (Using Level Order Traversal)
https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/

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

from collections import Counter, defaultdict, deque
import sys


class Node:
    def __init__(self, key: int):
        self.data = key
        self.left = None
        self.right = None


# my solution
class Solution:
    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root: Node) -> List[int]:
        # Your code here
        if root is None:
            return []
        # Create a map and store vertical order in map
        verticalOrderMap = dict()
        horizontalDistance = 0
        # Create queue to do level order traversal. Every item of queue contains node and horizontal distance.
        q = deque()
        q.append((root, horizontalDistance))
        while q:
            # pop from queue front
            temp = q.popleft()
            horizontalDistance = temp[1]
            node = temp[0]
            # insert this node's data in the map of lists
            if horizontalDistance not in verticalOrderMap:
                verticalOrderMap.update({horizontalDistance: [node.data]})
            else:
                verticalOrderMap[horizontalDistance].append(node.data)
            if node.left is not None:
                q.append((node.left, horizontalDistance-1))
            if node.right is not None:
                q.append((node.right, horizontalDistance+1))
        # Traverse the map and print nodes at every horizontal distance (hd)
        res = list()
        # Sort the map according to horizontal distance
        sortedVerticalOrderMap = collections.OrderedDict(sorted(verticalOrderMap.items()))
        for hd, vals in sortedVerticalOrderMap.items():
            for val in vals:
                res.append(val)
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
