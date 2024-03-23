class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0 
        end = len(nums) - 1

        left = -1
        right = -1

        while start<=end:
            
            mid = start + (end-start)//2
            # print(start,mid,end)
            if nums[mid] == target:
                if mid != 0:
                    if nums[mid-1] < target:
                        left = mid
                        break
                    else:
                        end = mid-1
                else:
                    left = 0
                    break
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        
        start = 0 
        end = len(nums) - 1

        while start<=end:
            
            mid = start + (end-start)//2
            # print(start,mid,end)
            if nums[mid] == target:
                if mid != len(nums)-1:
                    if nums[mid+1] > target:
                        right = mid
                        break
                    else:
                        start = mid+1
                else:
                    right = len(nums)-1
                    break
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1

        return [left, right]

