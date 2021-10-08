

# GeeksForGeeks Practice. Problem of the Day. October. Day 8. Cows of FooLand

'''


Cows of FooLand
Medium Accuracy: 50.8% Submissions: 2500 Points: 4

Cows in the FooLand city are interesting animals. One of their specialities is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of two years and proceeds to produce other calves (one female calf a year).

Now the farmer Harold wants to know how many animals would he have at the end of N years, if we assume that none of the calves dies, given that initially, he has only one female calf?

Since the answer can be huge, print it modulo 109+7.


Example 1:

Input: N = 2
Output: 2
Explanation: At the end of 1 year, he will have
only 1 cow, at the end of 2 years he will have
2 animals (one parent cow C1 and other baby
calf B1 which is the offspring of cow C1).

Example 2:

Input: N = 4
Output: 5
Explanation: At the end of 1 year, he will have
only 1 cow, at the end of 2 years he will have
2 animals (one parent cow C1 and other baby
calf B1 which is the offspring of cow C1). At
the end of 3 years, he will have 3 animals (one
parent cow C1 and 2 female calves B1 and B2, C1
is the parent of B1 and B2).At the end of 4
years,he will have 5 animals (one parent cow C1,
3 offsprings of C1 i.e. B1, B2, B3 and one
offspring of B1).



Your Task:
You don't need to read or print anything. Your task is to complete the function TotalAnimal() which takes N as input parameter and returns the total number of animals at the end of N years modulo 109 + 7.


Expected Time Complexity: O(log2N)
Expected Space Complexity: O(1)


Constraints:
1 <= N <= 1018

View Bookmarked Problems
Topic Tags
Mathematical



(N+1)-th Fibonacci Number in O(logN) using Matrix Exponentiation (Short Code)
Refer to - Matrix Exponentiation video tutorial - Errichto - Codeforces
https://codeforces.com/blog/entry/80195?mobile=true

void multiply(vector<vector<int64_t>> &a, vector<vector<int64_t>> &b) {
    vector<vector<int64_t>> c(2, vector<int64_t>(2, 0));
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int l=0;l<2;l++)(c[i][j]+=a[i][l]*b[l][j])%=((int)1e9 + 7);
        }
    }
    a = c;
}
int TotalAnimal(int64_t n) {
    vector<vector<int64_t>> ans(2, vector<int64_t>(2, 1)), d(2, vector<int64_t>(2, 1));
    d[1][1] = ans[0][1] = ans[1][0] = 0;
    while (n > 0) {
        if (n & 1)multiply(ans, d);
        multiply(d, d);
        n >>= 1;
    }
    return ans[0][0];
}


5 способов вычисления чисел Фибоначчи: реализация и сравнение
https://habr.com/ru/post/261159/

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


# my solution (memory error for very big input N)
class Solution2:
    def TotalAnimal(self, N: int) -> int:
        # Code here
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N > 2:
            dp = [0] * (N+1)
            dp[0] = 1
            dp[1] = 1
            dp[2] = 2
            # mod = 1e9 + 7
            mod = pow(10, 9) + 7
            for i in range(3, N + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return int(dp[N] % mod + 0.5)


class Solution3:
    def TotalAnimal(self, N: int) -> int:
        # Code here
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N > 2:
            mod = pow(10, 9) + 7
            SQRT5 = math.sqrt(5)
            PHI = (SQRT5 + 1) / 2
            res = int(PHI ** (N+1) / SQRT5 + 0.5)
            return int(res % mod + 0.5)


class Solution4:
    def TotalAnimal(self, N: int) -> int:
        # Code here
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N > 2:
            mod = pow(10, 9) + 7
            a = 0
            b = 1
            for __ in range(N+1):
                a, b = b, a + b
            return int(a % mod + 0.5)


class Solution:
    def myPow(self, x, n, I, mult):
        """
        Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
        перемножается с mult, а n – положительное целое
        """
        if n == 0:
            return I
        elif n == 1:
            return x
        else:
            y = self.myPow(x, n // 2, I, mult)
            y = mult(y, y)
            if n % 2:
                y = mult(x, y)
            return y

    def identity_matrix(self, n):
        """Возвращает единичную матрицу n на n"""
        r = list(range(n))
        return [[1 if i == j else 0 for i in r] for j in r]

    def matrix_multiply(self, A, B):
        BT = list(zip(*B))
        return [[sum(a * b
                     for a, b in zip(row_a, col_b))
                 for col_b in BT]
                for row_a in A]

    def fib(self, n):
        F = self.myPow([[1, 1], [1, 0]], n, self.identity_matrix(2), self.matrix_multiply)
        return F[0][1]

    def TotalAnimal(self, N: int) -> int:
        # Code here
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N > 2:
            mod = pow(10, 9) + 7
            res = self.fib(N+1)
            return int(res % mod + 0.5)


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
