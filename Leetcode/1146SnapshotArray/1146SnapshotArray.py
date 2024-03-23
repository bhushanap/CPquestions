class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.arr = [[(0,0)] for i in range(length)]
        self.snapid = 0
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.arr[index][-1][0] == self.snapid:
            self.arr[index][-1] = (self.snapid,val)
            return
        
        self.arr[index].append((self.snapid,val))
        
        

    def snap(self):
        """
        :rtype: int
        """
        
        self.snapid +=1
        return self.snapid-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # print(self.arr)
        tmp = self.arr[index]

        start = 0
        end = len(tmp)-1


        while start<=end:
            mid = start + (end-start)//2
            if tmp[mid][0] == snap_id:
                return tmp[mid][1]
            elif tmp[mid][0] > snap_id:
                end = mid-1
            else:
                if mid < len(tmp)-1:
                    if tmp[mid+1][0] <= snap_id:
                        start = mid+1
                    else:
                        return tmp[mid][1]
                else:
                    return tmp[mid][1]
        
        return tmp[mid][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)