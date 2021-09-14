

# GeeksForGeeks Practice. Problem of the Day. September. Day 14

'''


Remove loop in Linked List
Medium Accuracy: 47.96% Submissions: 100k+ Points: 4

Given a linked list of N nodes such that it may contain a loop.

    A loop here means that the last node of the link list is connected to the node at position X. If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present.


Example 1:

Input:
N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.


Example 2:

Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The Linked list does not
contains any loop.


Your Task:
You don't need to read input or print anything. Your task is to complete the function removeLoop() which takes the head of the linked list as input parameter. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.
Note: The generated output will be 1 if your submitted code is correct.


Expected time complexity : O(N)
Expected auxiliary space : O(1)


Constraints:
1 ≤ N ≤ 104

Company Tags
Adobe
Amazon
Goldman Sachs
Kuliza
MakeMyTrip
Microsoft
Morgan Stanley
Netskope
Oracle
Qualcomm
Snapdeal
VMWare
Walmart
Topic Tags
Linked List
Two-pointer-algorithm
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
Vmware interview experience set 9 internship rd
Walmart labs interview experience set 2 on campus
Makemytrip interview experience set 8 on campus
Adobe interview experience shecodes software engineer
W


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


# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head

        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            # If slow_p and fast_p meet at some point then
            # there is a loop
            if slow_p == fast_p:
                self.removeLoop(slow_p)

                # Return 1 to indicate that loop is found
                return 1

        # Return 0 to indicate that there is no loop
        return 0

        # Function to remove loop

    # loop_node --> pointer to one of the loop nodes
    # head --> Pointer to the start node of the linked list
    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node

        # Count the number of nodes in loop
        k = 1
        while (ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1

        # Fix one pointer to head
        ptr1 = self.head

        # And the other pointer to k nodes after head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next

        # Move both pointers at the same place
        # they will meet at loop starting node
        while (ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node
        while (ptr2.next != ptr1):
            ptr2 = ptr2.next

        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        llist = LinkedList()
        llist.head = head
        llist.detectAndRemoveLoop()


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
