"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)
"""

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #make a list of list where the index represents the length of the list at that index
        dp = []
        fib = [1,2]
        
        #for each number, if fibonacci, try and add it to the longest list until it fits
        for num in A:
            while fib[-1] < num:
                fib.append(fib[-1]+fib[-2])
                
            if num in fib:
                if len(dp) == 0:
                    dp.append([num])
                else:
                    for seq in dp[::-1]:
                        if num > seq[-1] and len(seq) == len(dp):
                            temp = seq + [num]
                            dp.append(temp)
                        else:                            
                            for i in range(len(seq) -1, -1 , -1):
                                if seq[i] < num:
                                    if i == len(seq) - 1:
                                        seq[i] = num
                                    elif seq[i+1] > num:
                                        seq[i+1] = num
                                        continue;

        
        return len(dp[-1])
