class MedianFinder:

    def __init__(self):

        self.low,self.high = [],[]
        

    def addNum(self, num: int) -> None:

        if self.high and num>self.high[0]:
            heapq.heappush(self.high,num)
        else:
            heapq.heappush(self.low,-1*num)
        
        if len(self.low)>len(self.high) + 1:
            val  = -1*heapq.heappop(self.low)
            heapq.heappush(self.high,val)
        if len(self.high)>len(self.low)+1:
            val  =heapq.heappop(self.high)
            heapq.heappush(self.low,-1*val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -1*self.low[0]
        elif len(self.high) > len(self.low):
            return self.high[0]
        return (-1*self.low[0]+self.high[0])/2.0
