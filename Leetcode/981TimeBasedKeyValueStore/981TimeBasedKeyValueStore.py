class TimeMap(object):

    def __init__(self):

        self.map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.map:
            self.map[key].append((timestamp,value)) 
        else:
            self.map[key] = [(timestamp,value)]
        # print(self.map)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.map:
            arr = self.map[key]
            start = 0
            end = len(arr)-1
            while start<=end:
                mid = start + (end-start)//2
                # print(start,mid,end,timestamp)
                if arr[mid][0]==timestamp:
                    return arr[mid][1]
                elif arr[mid][0]<timestamp:
                    if mid<len(arr)-1:
                        # print('hello')
                        if arr[mid+1][0]>timestamp:
                            # print('a')
                            return arr[mid][1]
                        else:
                            # print('b')
                            start = mid+1
                    else:
                        return arr[mid][1]    
                else:
                    end = mid-1
            return ""
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)