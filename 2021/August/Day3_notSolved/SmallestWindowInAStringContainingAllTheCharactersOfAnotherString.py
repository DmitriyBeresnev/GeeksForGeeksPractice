

# Smallest window in a string containing all the characters of another string

'''


Smallest window in a string containing all the characters of another string
Medium Accuracy: 42.59% Submissions: 30663 Points: 4

Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output:
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.

Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output:
apzo
Explanation: "apzo" is the smallest
substring in which "oza" can be found.

Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S|, |P| ≤ 105




Company Tags:
Amazon
Google
MakeMyTrip
Streamoid Technologies
Microsoft
Media.net

Topic Tags:
Hash
Sliding-window
Strings
Dynamic Programming



https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

https://www.geeksforgeeks.org/python-get-the-smallest-window-in-a-string-containing-all-characters-of-given-pattern/

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
no_of_chars = 256


# my solution (found in the inet)
class Solution:
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, string, pat):
        len1 = len(string)
        len2 = len(pat)

        # Check if string's length is
        # less than pattern's
        # length. If yes then no such
        # window can exist
        if len1 < len2:
            print("No such window exists")
            return ""

        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars

        # Store occurrence ofs characters of pattern
        for i in range(0, len2):
            hash_pat[ord(pat[i])] += 1

        start, start_index, min_len = 0, -1, float('inf')

        # Start traversing the string
        count = 0  # count of characters
        for j in range(0, len1):

            # count occurrence of characters of string
            hash_str[ord(string[j])] += 1

            # If string's char matches with
            # pattern's char then increment count
            if (hash_str[ord(string[j])] <=
                    hash_pat[ord(string[j])]):
                count += 1

            # if all the characters are matched
            if count == len2:

                # Try to minimize the window
                while (hash_str[ord(string[start])] >
                       hash_pat[ord(string[start])] or
                       hash_pat[ord(string[start])] == 0):

                    if (hash_str[ord(string[start])] >
                            hash_pat[ord(string[start])]):
                        hash_str[ord(string[start])] -= 1
                    start += 1

                # update window size
                len_window = j - start + 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start

        # If no window found
        if start_index == -1:
            # print("No such window exists")
            return -1

        # Return substring starting from
        # start_index and length min_len
        return string[start_index: start_index + min_len]


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
