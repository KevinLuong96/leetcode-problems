"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right + 1):
            digits = list(str(i))
            if len(digits) == 1:
                ans.append(i)
                continue 
            
            selfDividing = True
            for digit in digits:
                if int(digit) == 0 or i % int(digit) != 0:
                    selfDividing = False
                    break
            if selfDividing:
                ans.append(i)
            
        return ans