class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1
        
        while start<end-1:
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                if nums[start]>target:
                    if nums[mid]>nums[start]:
                        start=mid+1
                    else:
                        end=mid-1
                elif nums[start]==target:
                    return start
                else:
                    end=mid-1
            elif nums[mid]<target:
                if nums[end]<target:
                    if nums[end]>nums[mid]:#t6 m3 e5
                        end=mid-1
                    else:#m3 t6 e2
                        start=mid+1
                elif nums[end]==target:#m6 t10 e12
                    return end
                else:
                    start=mid+1
        if start>=end-1:
            if nums[start]==target:
                return start
            if nums[end] == target:
                return end
        return -1
        