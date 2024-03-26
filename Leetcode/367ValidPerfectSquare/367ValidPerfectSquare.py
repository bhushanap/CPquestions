class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        while start<=end:
            mid = start + (end-start)//2
            print(mid)
            if mid*mid==num:
                return mid
            elif mid*mid>num:
                end=mid-1
            else:
                start=mid+1

            
        