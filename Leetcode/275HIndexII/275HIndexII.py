class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start = 0
        end = len(citations)

        while start<end:
            mid = start + (end-start)//2
            if citations[mid]>=len(citations)-mid:
                end = mid
                if mid == 0:
                    return len(citations)
            else:
                start = mid + 1
        return len(citations)-end
        