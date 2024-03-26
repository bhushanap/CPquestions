class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = start+(end-start)//2
            print(arr[mid])
            if arr[mid]==mid+k+1:
                if (arr[mid-1]<arr[mid]-1 or mid==0):
                    return arr[mid]-1
                else:
                    i = 2
                    while True:
                        if arr[mid-i]<arr[mid]-i:
                            return arr[mid]-i
                        i+=1
            elif arr[mid]>mid+k+1:
                if mid==0:
                    break
                else:
                    if arr[mid-1] < mid+k:
                        break
                end=mid-1
            else:
                start=mid+1
        
        if arr[-1] < len(arr)+k:
            return k + len(arr)
        else:
            return mid+k