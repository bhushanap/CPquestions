class Solution(object):
    def mySqrt(self, num):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = num
        while start<end-1:
            
            mid = start + (end-start)//2
            # print(mid)
            if mid*mid==num:
                return mid
            elif mid*mid>num:
                end=mid-1
            else:
                start=mid
        
        if start==end-1:
            if end*end<=num:
                return end
            else:
                return start
        
        return start

           