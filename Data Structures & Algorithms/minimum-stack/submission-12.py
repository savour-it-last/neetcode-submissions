class MinStack:

    def __init__(self):
        self.stack = []
        self.minheap = []
        self.minimums = []
        self.curr_min = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minheap, val)
        if not self.minimums or (self.curr_min is not None and val < self.curr_min):
            self.minimums.append(val)
            self.curr_min = val
        elif self.curr_min is not None:
            self.minimums.append(self.curr_min)
        else:
            print("ERROR")
        

    def pop(self) -> None:
        val = self.stack.pop()
        self.minimums.pop(-1)
        if self.minimums:
            self.curr_min = self.minimums[-1]
        else:
            self.curr_min = None
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]

        
