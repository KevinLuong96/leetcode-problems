"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        #make two pointers and find where one is <x and the other >x
        #take the lower value of the two and add to ans
        if len(arr) == 1 and k ==1 :
            return arr
        
        p1,p2 = 0, 1
        
        for i in range(len(arr)): 
            print(p1,p2)

            
            #if the first number is greater than the target, return the first k values
            if i == 0 and arr[i] > x:
                return arr[:k]
            #if the last number is smaller than the target, return the last k values
            if i == len(arr) - 2:
                if arr[p2] < x:
                    return arr[::-1][:k]
            
            elif arr[i]<=x and arr[i+1]>x:
                p1, p2 = i, i+1;
                
        ans = []
        for i in range(k):
            # print(abs(arr[p2]-x),abs(arr[p1]-x))
            if abs(arr[p2]-x) < abs(arr[p1]-x) or p1 == -1:
                ans.append(arr[p2])
                p2 = p2 + 1 if p2 + 1 < len(arr) else -1
            
            elif abs(arr[p1]-x) <= abs(arr[p2]-x) or p2 == -1:
                ans.append(arr[p1])
                p1 = p1 - 1 if p1 -1 >= 0 else -1
                
        return ans
