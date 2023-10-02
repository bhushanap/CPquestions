class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0 
        last = len(nums)-1
        while first<last-1:
            mid  = (first+last) //2 
            if nums[mid]>target:
                last = mid
            elif nums[mid]<target:
                first = mid
            else:
                return mid

        if nums[first]==target:
            return first
        elif target>nums[last]:
            return last+1
        elif target<nums[first]:
            return first
        else:
            return last
