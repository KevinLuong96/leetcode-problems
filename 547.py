"""
Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations 
is the substring of the second string.
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        #turn s1 into a map of char counts
        s1chars = {};
        for c in s1:
            s1chars[c] = s1chars.get(c, 0) + 1
        
        #use a sliding window on s2 to get char counts at the current starting char
        i = 0
        s2chars = {};
        
        for k in range(len(s1)):
            char = s2[k];
            s2chars[char] = s2chars.get(char, 0) + 1
            
        if s1chars == s2chars:
            return True
        
        #iterate on the difference in length between the strings
        for j in range(len(s1), len(s2)):
            #remove the trailing char and delete the key if the count for that char is 0
            prev = s2[i]
            s2chars[prev] -= 1 
            if s2chars[prev] == 0:
                s2chars.pop(prev)
            i += 1
                
                
            #add the next char
            n = s2[j]
            s2chars[n] = s2chars.get(n,0) + 1
            
            if s1chars == s2chars:
                return True
            
        return False
                
            
            
            
        