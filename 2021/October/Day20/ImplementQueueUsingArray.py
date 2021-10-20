

# GeeksForGeeks Practice. Problem of the Day. October. Day 20. Implement Queue using array

'''


Implement Queue using array
Basic Accuracy: 48.28% Submissions: 49130 Points: 1

Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

Example 1:

Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation:
In the first test case for query
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3

Example 2:

Input:
Q = 4
Queries = 1 3 2 2 1 4
Output: 3 -1
Explanation:
In the second testcase for query
1 3 the queue will be {3}
2   poped element will be 3 the
    queue will be empty
2   there is no element in the
    queue and hence -1
1 4 the queue will be {4}.

Your Task :
You are required to complete the two methods push() which take one argument an integer 'x' to be pushed into the queue and pop() which returns a integer poped out from othe queue. If the queue is empty, it should return -1 on a pop operation.

Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 ≤ Q ≤ 105
1 ≤ x ≤ 105

View Bookmarked Problems
Company Tags
Goldman Sachs
Amazon
Topic Tags
Arrays
Queue
Related Courses
DSA-Self Paced with Doubt Assistance
Data Structures and Algorithms
Amazon SDE Test Series
Placement 100
DS and Algo Foundation
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Data Structures With Python
Competitive Programming - Live
DSA Live for Working Professionals
First Step to Data Structures and Algorithms



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


# my solution
class MyQueue:
    def __init__(self):
        self.q = []
        self.head = 0
        self.tail = 0

    # Function to push an element x in a queue.
    def push(self, x: int) -> None:
        # add code here
        self.q.append(x)
        self.tail += 1

    # Function to pop an element from queue and return that element.
    def pop(self) -> int:
        # add code here
        val = -1
        if self.q and self.head != self.tail:
            val = self.q[self.head]
            self.head += 1
        return val


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
