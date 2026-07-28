class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        registry = {}
        for task in tasks:
            if task not in registry:
                registry[task]=0
            registry[task]+=1
        
        max_heap = []

        for count in registry.values():
            heapq.heappush(max_heap, -count)

        cooldown_q = collections.deque()
        time = 0
        while max_heap or cooldown_q:
            time+=1
            if max_heap:
                neg_count = heapq.heappop(max_heap)
                count = -neg_count - 1
                if count > 0:
                    cooldown_q.append((time+n, count))

            if cooldown_q and cooldown_q[0][0]==time:
                _, remaining = cooldown_q.popleft()
                heapq.heappush(max_heap, -remaining)
        return time
        
                