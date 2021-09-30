

# GeeksForGeeks Practice. Problem of the Day. September. Day 28. Sort a stack

'''


Sort a stack
Easy Accuracy: 50.51% Submissions: 53126 Points: 2

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1

Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2

Your Task:
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.

Constraints:
1<=N<=100

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

Company Tags
Amazon
Goldman Sachs
IBM
Intuit
Kuliza
Yahoo
Microsoft
Topic Tags
Recursion
Stack
STL
Related Courses
Amazon SDE Test Series
Microsoft SDE Test Series
Placement Guide 2021-2022





#include<bits/stdc++.h>
using namespace std;

void insert_at_correct_pos(stack<int> &s, int i){

	//if current element is larger than all elements of stack
    if(s.empty() || s.top()<=i){
        s.push(i);
        return;
    }

    int t = s.top();
    s.pop();
    insert_at_correct_pos(s, i);
    s.push(t);
    return;
}

void emptystack(stack<int> &s){
    if(s.empty()){
        return;
    }
    int i = s.top();
    s.pop();
    emptystack(s);
    insert_at_correct_pos(s, i);
}

int main(){
    stack<int> s;
    s.push(1); s.push(20); s.push(53); s.push(10); s.push(2); s.push(31);
    emptystack(s);
    while(!s.empty()){
        cout<<s.top()<<" ";
        s.pop();
    }
}

//using multiset
void SortedStack :: sort(){
   int n = s.size();
   multiset<int> a;
   while(n--){
       a.insert(s.top());
       s.pop();
   }
   for(int i: a){
       s.push(i);
   }
}


concept :- See here in that problem we have a stack means LIFO right, means last in first out right ok. so here we have to sort such that the largest element is present at the top . One more thing is that the way array work is same as stack just think if we append some element it goes to top and when we pop it it removes from top right.

===> Now what we do simply think in a way if you have two elements let suppose  s = [1,2] right it means at top we have 1 ok and in that problem largest element should be at top like that [2,1] right so we simply pop 2 and 1 and store it some where ok now stack is empty and everything should be removed and put it in some variable ok. Now we first push 1 in stack as stack is empty and 1  is the largest element right.Now  we have 2 to push in stack but before that we check if the element which is at top is less or greater and 1 is smaller than 2 now we remove 1  and push 2  first and then again push 1  so at last we get 2 top and 1 below that  and yeah we sort it as [2,1].

OKoK now let see the code :-

class Solution:
   def sortedInsert(self,s , element):
       if len(s) == 0 or element > s[-1]:
           s.append(element)
           return
       else:
           temp = s.pop()
           self.sortedInsert(s, element)
           s.append(temp)

   def sortedHelper(self,s):
       if len(s) != 0:
           temp = s.pop()
           self.sortedHelper(s)
           self.sortedInsert(s , temp)

   def sorted(self, s):
       self.sortedHelper(s)
       s.reverse()



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
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s: List[int]):
        # Code here
        stackSize = len(s)
        if stackSize == 0 or stackSize == 1:
            return s
        return s.sort(reverse=True)


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
