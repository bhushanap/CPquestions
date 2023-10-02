class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        mid = (first + last)//2
        loop = 3
        while True:
            print(first, mid, last)
            if target>nums[mid]:
                first = mid
            elif target<nums[mid]:
                last = mid
            else:
                return mid
            mid = (first + last)//2 
            if first>=last-1:
                if target==nums[first]:
                    return first
                elif first==last:
                    return -1
                elif target==nums[last]:
                    return last
                else:
                    return -1
            
            
        
        return nums[midi]