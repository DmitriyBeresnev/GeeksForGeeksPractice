

# GeeksForGeeks Practice. Problem of the Day. September. Day 15. Sort an array of 0s, 1s and 2s

'''


Sort an array of 0s, 1s and 2s
Easy Accuracy: 51.36% Submissions: 100k+ Points: 2

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input:
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated
into ascending order.

Example 2:

Input:
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated
into ascending order.


Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2

Company Tags
Adobe
Amazon
Hike
MakeMyTrip
MAQ Software
Microsoft
Morgan Stanley
Ola Cabs
OYO Rooms
Paytm
Qualcomm
Samsung
SAP Labs
Snapdeal
Walmart
Yatra.com
Topic Tags
Arrays
Sorting
Related Courses
Must Do Interview Preparation
TCS NQT Mock Test Series
Placement 100
Complete Interview Preparation
Complete Interview Preparation With Doubt Assistance
Microsoft SDE Test Series
Must Do Coding Questions
Related Interview Experiences
Paytm interview experience set 14 for senior android developer
Ola cabs interview experience set 4 for sde 2
Paytm interview experience set 5 recruitment drive
Amazon interview experience for sde intership



2 solutions

//1)Using DNF (Dutch National Flag) algorithm
void sort012(int a[], int n)
    {
        // code here
        int low = 0,mid = 0,high = n - 1;
       while(mid <= high)
       {
           if(a[mid] == 0)
           {
               swap(a[low], a[mid]);
               low++;
               mid++;
           }
           else if(a[mid] == 1)
           {
               mid++;
           }
           else if(a[mid] == 2)
           {
               swap(a[mid], a[high]);
                   high--;
            }
        }
    }

//2)Using simple counting
void sort012(int a[], int n)
    {
        // code here
        int count0= 0,count1 =0,count2=0,i;
        for(i=0;i<n;i++)
        {
            if(a[i]==0)
                count0++;
            else if(a[i]==1)
                count1++;
            else if(a[i]==2)
                count2++;
        }
        for(i=0;i<count0;i++)
            a[i]=0;
        for(i=count0;i<count0+count1;i++)
            a[i]=1;
        for(i=count0+count1;i<count0+count1+count2;i++)
            a[i]=2;
    }

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
class Solution:
    def sort012(self, arr: List[int], n: int):
        # code here
        return arr.sort()


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
