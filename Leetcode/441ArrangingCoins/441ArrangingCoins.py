class Solution(object):
    def arrangeCoins(self, num):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = num
        while start<end-1:
            
            mid = start + (end-start)//2
            # print(mid)
            if mid*(mid+1)/2==num:
                return mid
            elif mid*(mid+1)/2>num:
                end=mid-1
            else:
                start=mid
        
        if start==end-1:
            if end*(end+1)/2<=num:
                return end
            else:
                return start
        
        return start
        