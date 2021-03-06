

# Construct Tree from Preorder Traversal

'''


Construct Tree from Preorder Traversal
Medium Accuracy: 50.68% Submissions: 11825 Points: 4

Construct a binary tree of size N using two given arrays pre[] and preLN[]. Array pre[] represents preorder traversal of a binary tree. Array preLN[] has only two possible values ‘L’ and ‘N’. The value ‘L’ in preLN[] indicates that the corresponding node in Binary Tree is a leaf node and value ‘N’ indicates that the corresponding node is a non-leaf node.
Note: Every node in the binary tree has either 0 or 2 children.

Example 1:

Input :
N = 5
pre[] = {10, 30, 20, 5, 15}
preLN[] = {N, N, L, L, L}

Output:
          10
        /    \
      30      15
     /  \
   20    5



Your Task:
You dont need to read input or print anything. Complete the function constructTree() which takes N, pre[] and preLN[] as input parameters and returns the root node of the constructed binary tree.
Note: The output generated by the compiler will contain the inorder traversal of the created binary tree.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 104
1 ≤ pre[i] ≤ 107
preLN[i]: {'N', 'L'}

Company Tags
Amazon
Hike
Topic Tags
Traversal
Tree
Related Courses
Amazon SDE Test Series



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
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''
class BST:
    def __init__(self, node: Node):
        self.root = node

    def insert(self, node: Node, curNode: Node):
        if (node.data < curNode.data):
            if (curNode.left != None):
                self.insert(node, curNode.left)
            else:
                curNode.left = node
        else:
            if (curNode.right != None):
                self.insert(node, curNode.right)
            else:
                curNode.right = node
'''

'''
def reconstruct(index: int, pre: List[int], preLN: List[str], n: int) -> Node:
    if index >= n:
        return None
    if preLN[index] == "L":
        node = Node(pre[index])
        index += 1
        return node
    node = Node(pre[index])
    index += 1
    node.left = reconstruct(index, pre, preLN, n)
    node.right = reconstruct(index+1, pre, preLN, n)
    return node
'''

def reconstruct(index: int, pre: List[int], preLN: List[str], n: int) -> Node:
    if index >= n:
        return None
    node = Node(pre[index])
    if preLN[index] != "L":
        index += 1
        node.left = reconstruct(index, pre, preLN, n)
        index += 1
        node.right = reconstruct(index, pre, preLN, n)
    return node


# my solution (found in the inet)
def constructTree(pre: List[int], preLN: List[str], n: int) -> Node:
    # code here
    k = 0
    #root = Node(pre[0])
    root = reconstruct(k, pre, preLN, n)
    return root


if __name__ == "__main__":
    #
    start = time.perf_counter()
    print(constructTree(pre = [10, 30, 20, 5, 15], preLN = ['N', 'N', 'L', 'L', 'L'], n = 5)) #
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
