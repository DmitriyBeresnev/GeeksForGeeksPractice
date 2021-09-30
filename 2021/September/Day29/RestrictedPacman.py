

# GeeksForGeeks Practice. Problem of the Day. September. Day 29. Restricted Pacman

'''


Restricted Pacman
Medium Accuracy: 89.24% Submissions: 2189 Points: 4

In the game of Restricted Pacman, an infinite linear path is given. Pacman has to start at position 0 and eat as many candies as possible. In one move he can only jump a distance of either M or N.  If M and N are coprime numbers, find how many candies will be left on the board after the game is over.
Note: The result is always finite as after a point X every index in the infinite path can be visited.

Example 1:

Input: M = 2, N = 5
Output: 2
Explanation: From index 0, the indices that
can be visited are
0 + 2 = 2
0 + 2 + 2 = 4
0 + 5 = 5
0 + 2 + 2 + 2 = 6
0 + 2 + 5 = 7
0 + 2 + 2 + 2 + 2 = 8
0 + 2 + 2 + 5 = 9
0 + 5 + 5 = 10
and so on.
1 and 3 are the only indices that cannot be
visited. Therefore the candies at these two
positions will be left on the board.


Example 2:

Input: M = 2, N = 7
Output: 3

Example 3:

Input: M = 25, N = 7
Output: 72

Your Task:
You don't need to read input or print anything. Complete the function candies() which take M and N as input parameters and return the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 < M, N ≤ 500

Topic Tags
Queue
Mathematical
Hash



Frobenius Number and Coin Problem
https://en.wikipedia.org/wiki/Coin_problem

Even if you don't know anything about Frobenius Number and Coin Problem, you can solve it with an algorithm using a Hashset:

Hashset will represent the set of candies which can be eaten.
Add M, N into Hashset.
Loop with every integer I, starting from min(M, N) + 1 {
	if Hashset contains either I - M or I - N {
		add I into Hashset.
		if I is added "min(M, N)" times consecutively, We're sure there will be no more candies left uneaten afterwards.
		The total amount of uneaten candies is I - "size of Hashset".
	}
}


int candies(int m, int n) {
    vector<bool> dp(m * n + 1, false);
    dp[0] = true;
    int ans = 0;
    for (int i = 1; i <= m * n; i++) {
        if (i >= m)dp[i] = dp[i] | dp[i - m];
        if (i >= n)dp[i] = dp[i] | dp[i - n];
        if (!dp[i])ans++;
    }
    return ans;
}


static int candies(int m, int n)
   {

       int maxRange = lcm(m, n);

       HashMap<Integer, Integer> map = new HashMap<>();

       map.put(0, 1);


       int count = 0;

       for(int i = 1; i < maxRange; i++)
       {
           if(map.containsKey(i - n) || map.containsKey(i - m))
           {
               map.put(i, 1);
           }
           else
           {
               count += 1;
           }
       }


       return count;
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
    def candies(self, m: int, n: int) -> int:
        # Your code goes here
        '''
        int max = (m*n)-m-n; // frobenius method
        int  count = max/2 +1;
        return count;
        '''
        return int((m - 1) * (n - 1) / 2)


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
