

# GeeksForGeeks Practice. Problem of the Day. September. Day 26. Count Occurences of Anagrams

'''


Count Occurences of Anagrams
Medium Accuracy: 50.78% Submissions: 12452 Points: 4

Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.

Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.

Your Task:
Complete the function search() which takes two strings pat, txt, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(26) or O(256)

Constraints:
1 <= |pat| <= |txt| <= 105
Both string contains lowercase english letters.



Company Tags
Amazon
Intuit
Microsoft
Topic Tags
Arrays
Sliding-window
Related Interview Experiences
Intuit interview set 8 on campus
Intuit interview set 9 on campus



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
    def search(self, pat: str, txt: str) -> int:
        text = txt
        word = pat
        nText = len(text)
        windiwSize = len(word)
        nWindowShifts = nText - windiwSize + 1
        #symbolsFreqMap = Counter(word)
        symbolsSeq = sorted(word)
        anagramsCount = 0
        for i in range(nWindowShifts):
            wordInText = text[i: i + windiwSize]
            #if symbolsFreqMap == Counter(wordInText):
            if symbolsSeq == sorted(wordInText):
                anagramsCount += 1
        return anagramsCount


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.findAnagrams("forxxorfxdofr", "for")) #
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
