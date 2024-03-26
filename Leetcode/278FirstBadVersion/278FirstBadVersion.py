# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        last = False
        while last==False:
            mid = start + (end-start)//2
            bad = isBadVersion(mid)
            if bad:
                if mid>0:
                    if isBadVersion(mid-1):
                        end = mid-1
                    else:
                        return mid
                else:
                    return 1
            else:
                if mid<n:
                    if isBadVersion(mid+1):
                        return mid+1
                    else:
                        start = mid+1
                else:
                    pass
        