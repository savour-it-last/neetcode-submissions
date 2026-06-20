class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        
    def findMedian(self) -> float:
        self.stream.sort()
        n = len(self.stream)
        half = n//2
        if n==1:
            median = self.stream[0]
        elif n%2 != 0:
            median = float(self.stream[half])
        else:
            median = (self.stream[half-1] + self.stream[half])/2
        return median
        
        
        