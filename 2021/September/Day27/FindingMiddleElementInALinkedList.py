

# GeeksForGeeks Practice. Problem of the Day. September. Day 27. Finding middle element in a linked list

'''


Finding middle element in a linked list
Easy Accuracy: 47.37% Submissions: 100k+ Points: 2

Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 3
Explanation:
Middle of linked list is 3.

Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 7
Explanation:
Middle of linked list is 7.

Your Task:
The task is to complete the function getMiddle() which takes a head reference as the only argument and should return the data at the middle node of the linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 5000

Company Tags
Adobe
Amazon
Flipkart
GE
Hike
IgniteWorld
MAQ Software
Microsoft
Morgan Stanley
Nagarro
Netskope
Payu
Qualcomm
Samsung
SAP Labs
Veritas
VMWare
Wipro
Zoho
Topic Tags
Linked List
Related Courses
Must Do Interview Preparation
Amazon SDE Test Series
Microsoft SDE Test Series
Google Test Series
Must Do Coding Questions
Related Interview Experiences
Vmware interview experience set 4 campus
Veritas interview experience set 2 campus



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
        self.next = None


# my solution
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head: Node) -> int:
        # Code here
        # return the value stored in the middle node
        slowPointer = head
        fastPointer = head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return slowPointer.data


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
