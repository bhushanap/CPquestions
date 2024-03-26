class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 1
        end = len(arr)-1
        while start<end:
            mid = start + (end-start)//2
            # print(start,mid,end)
            if mid != 0 and mid != len(arr)-1:
                if arr[mid-1]<arr[mid]:
                    if arr[mid]>arr[mid+1]:
                        return mid
                    else:
                        start = mid+1
                else:
                    end = mid
        return mid
            
