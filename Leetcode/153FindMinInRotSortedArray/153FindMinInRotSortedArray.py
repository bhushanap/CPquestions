class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        
        while start<=end:
            if nums[start]<nums[end]:
                return nums[start]
            
            mid = start + (end-start)//2
            # print(start,mid,end)
            if nums[mid]>=nums[start]:
                start = mid + 1
            else:
                if nums[mid-1]>nums[mid]:
                    return nums[mid]
                else:
                    end = mid - 1

        return nums[mid]
                
        