# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        gue = -1
        while gue!=0:
            mid = start+(end-start)//2
            gue = guess(mid)
            if gue>0:
                start = mid + 1
            else:
                end = mid - 1
            
        return mid
        