class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = (len(nums)-1)//2
        start = 0
        end = pairs
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[1]:
            return nums[0]
        if nums[-2]<nums[-1]:
            return nums[-1]
        while start<=end:
            mid = start + (end-start)//2
            print(start,mid,end)
            if nums[2*mid] < nums[2*mid+1]:
                if nums[2*mid-1]<nums[2*mid]:
                    return nums[2*mid]
                else:
                    end = mid-1
            else:
                start = mid+1
        