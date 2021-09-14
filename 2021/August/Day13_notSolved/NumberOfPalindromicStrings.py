

# Number of palindromic strings

'''


Number of palindromic strings
Medium Accuracy: 48.3% Submissions: 145 Points: 4

Given two integers N and K, the task is to find the count of palindromic strings of length lesser than or equal to N, with first K characters of lowercase English language, such that each character in a string doesn’t appear more than twice.

Note: Anwer can be very large, so, output answer modulo 109+7

Example 1:

Input: N = 3, K = 2
Output: 6
Explanation: The possible strings are:
"a", "b", "aa", "bb", "aba", "bab".

Example 2:

Input: N = 4, K = 3
Output: 18
Explanation: The possible strings are:
"a", "b", "c", "aa", "bb", "cc", "aba",
"aca", "bab", "bcb", "cac", "cbc",
"abba", "acca", "baab", "bccb", "caac",
"cbbc".

Your task:
You do not need to read any input or print anything. The task is to complete the function palindromicStrings(), which takes two integers as input and returns the count.

Expected Time Complexity: O(K2)
Expected Auxiliary Space: O(K2)

Constraints:
1 ≤ K ≤ 26
1 ≤ N ≤ 52
N ≤ 2*K

Topic Tags
Combinatorial
Dynamic Programming
Mathematical
Strings




from Comments

 Krishna • 8 hours ago • edited

If n=1, no. of ways=k.
if n=2, no. of ways=k,
if n=3, no.of ways=k*(k-1)
if n=4, no. of ways=k*(k-1)
if n=5, no. of ways=k*(k-1)*(k-2)
if n=6, no. of ways=k*(k-1)*(k-2)

and so on...
Finally, add all the number of ways from 1 to n.

TC: O(n), SC: O(n)
int palindromicStrings(int n, int k)
{
long long d=1000000007;
long long dp[n+1],p,i,s=0;
dp[0]=0,dp[1]=k;
if(n<=1)
return dp[n];
dp[2]=k;
for(i=3;i<=n;i++){
p=(i-1)/2;
dp[i]=(dp[i-2]*(k-p))%d;
}
for(i=1;i<=n;i++)
s=(s+dp[i])%d;
return s;
}

Here, for a given n, we need to add all the ways from 1 to n i.e. for n=2, ans=k+k=2k. In the last loop, I'm doing the sum.
In my above answer, no. of ways represents ans for exactly n(not after the summation).

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


# my solution (found in the inet)
class Solution:
    def palindromicStrings(self, N: int, K: int) -> int:
        # code here
        mod = 1000000007
        res = 0
        p = 0
        dp = [0] * (N+1)
        dp[1] = K
        if N <= 1:
            return dp[N]
        else:
            dp[2] = K
            for i in range(3, N+1):
                p = (i - 1) // 2
                dp[i] = dp[i-2] * (K - p) % mod
            for i in range(1, N + 1):
                res = (res + dp[i]) % mod
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.palindromicStrings(N = 3, K = 2)) #
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.palindromicStrings(N = 4, K = 3)) #
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
