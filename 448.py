"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #easy solution, make a list and when a number is found incrememnt
        #the list at index equal to value, count any indicies equal to 0
        
        temp = [0]* (len(nums) + 1)
        for num in nums:
            temp[num] += 1
            
        ans = []
        for i in range (1, len(temp)):
            if temp[i] == 0:
                ans.append(i)
                
        return ans
        
            
            
        
        