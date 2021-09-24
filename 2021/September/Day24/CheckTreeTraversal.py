

# GeeksForGeeks Practice. Problem of the Day. September. Day 24. Check Tree Traversal

'''


Check Tree Traversal
Hard Accuracy: 43.33% Submissions: 3100 Points: 8

Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.

Example 1:

Input:
N = 5
preorder[] = {1, 2, 4, 5, 3}
inorder[] = {4, 2, 5, 1, 3}
postorder[] = {4, 5, 2, 3, 1}
Output: Yes
Explanation:
All of the above three traversals
are of the same tree.
           1
         /   \
        2     3
      /   \
     4     5

Example 2:

Input:
N = 5
preorder[] = {1, 5, 4, 2, 3}
inorder[] = {4, 2, 5, 1, 3}
postorder[] = {4, 1, 2, 3, 5}
Output: No
Explanation: The three traversals can
not be of the same tree.


Your Task:
You don't need to read input or print anything. Complete the function checktree() which takes the array preorder[ ], inorder[ ], postorder[ ] and integer N as input parameters and returns true if the three traversals are of the same tree or not.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 103

Topic Tags
Recursion
Tree



Construct Tree from given Inorder and Preorder traversals
https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


I actually built the tree using inorder and preorder traversals, and then compared its postorder traversal with the given postorder array.

For building the tree, we store positions of every element of inorder traversal array in a hashmap. And we go step by step through the preorder array, recursively building the tree in valid (start, end) ranges which we obtain through the hashmap.

While building the tree though, there can be 2 invalid cases:

1) The node does not exist in our hashmap

2) The position of the node is either < start or > end


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
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# my solution
class Solution:
    preIndex = 0
    treeDataMap = dict()
    isPossible = True

    # This function mainly creates an
    # unordered_map
    def buldTreeMap(self, inOrderArr: List[int], nArr: int):
        # Store indexes of all items so that we
        # we can quickly find later
        # unordered_map<int, int>
        for i in range(nArr):
            self.treeDataMap[inOrderArr[i]] = i

    """
    # Recursive function to construct binary of size
    # len from Inorder traversal in[] and Preorder traversal
    # pre[]. Initial values of inStrt and inEnd should be
    # 0 and len -1. The function doesn't do any error
    # checking for cases where inorder and preorder
    # do not form a tree
    """
    def buildTree(self, inOrder: List[int], preOrder: List[int], inStrt: int, inEnd: int) -> Node:
        if (inStrt > inEnd):
            return None
        if not self.isPossible:
            return None
        # Pick current node from Preorder traversal using preIndex and increment preIndex
        curr = preOrder[self.preIndex]
        self.preIndex += 1
        tNode = Node(curr)
        # If this node has no children then return
        if (inStrt == inEnd):
            return tNode
        # Else find the index of this node in Inorder traversal
        #inIndex = self.treeDataMap[curr]
        inIndex = self.treeDataMap.get(curr)
        # check if curr data exist in treeDataMap
        if inIndex is None:
            self.isPossible = False
            return None
        # check if inIndex is not out of the range
        if inIndex < inStrt or inIndex > inEnd:
            self.isPossible = False
            return None
        # Using index in Inorder traversal, construct left and right subtress
        tNode.left = self.buildTree(inOrder, preOrder, inStrt, inIndex - 1)
        tNode.right = self.buildTree(inOrder, preOrder, inIndex + 1, inEnd)
        return tNode

    # Function to find index of value in arr[start...end]
    # The function assumes that value is present in inOrder[]
    def search(self, arr: List[int], start: int, end: int, value: int) -> int:
        for i in range(start, end + 1):
            if arr[i] == value:
                return i

    def printInorder(self, node):
        if node is None:
            return
        # first recur on left child
        self.printInorder(node.left)
        # then print the data of node
        print(node.data)
        # now recur on right child
        self.printInorder(node.right)

    def constructPostorderArr(self, root: Node, constructingPostorderArr: List[int]) -> None:
        if root is None:
            return None
        self.constructPostorderArr(root.left, constructingPostorderArr)
        self.constructPostorderArr(root.right, constructingPostorderArr)
        constructingPostorderArr.append(root.data)

    def checktree(self, preorder: List[int], inorder: List[int], postorder: List[int], N: int) -> bool:
        # Your code goes here
        self.buldTreeMap(inorder, N)
        root = self.buildTree(inorder, preorder, 0, len(inorder) - 1)
        constructingPostorderArr = list()
        if root is not None:
            self.constructPostorderArr(root, constructingPostorderArr)
        else:
            return False
        return postorder == constructingPostorderArr


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    N = 5
    preorder = [1, 2, 4, 5, 3]
    inorder = [4, 2, 5, 1, 3]
    postorder = [4, 5, 2, 3, 1]
    print(solution.checktree(preorder=preorder, inorder=inorder, postorder=postorder, N=N)) # Yes
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    N = 5
    preorder = [16, 1, 32, 37, 25]
    inorder = [32, 1, 37, 16, 25]
    postorder = [32, 37, 1, 25, 16]
    solution = Solution()
    print(solution.checktree(preorder=preorder, inorder=inorder, postorder=postorder, N=N)) # Yes
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
