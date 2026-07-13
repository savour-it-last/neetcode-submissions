class TimeMap:

    def __init__(self):
        self.timestamp_dict: dict[str, tuple[list[str], list[int]]] = {}
    
    def binary_search(self, timestamps: list[int], threshold: int) -> int:
        # NOTE: -1 if no value equal to or below the threshold is found.
        left = 0
        right = len(timestamps) - 1
        middle = (left+right)//2
        if timestamps[left]>threshold:
            return -1
        # this is a bit confusing when we gotta pick less that threshold.
        # so in that case while condition would fail so that middle would be true.
        while left <= right:
            middle = (left+right)//2
            if timestamps[middle] ==  threshold:
                return middle
            elif timestamps[middle]>threshold:
                right= middle -1
            else:
                left = middle + 1
        return right

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_dict:
            self.timestamp_dict[key] = ([], [])
        # NOTE: No need to sort since its given that its increasing
        self.timestamp_dict[key][0].append(value)
        self.timestamp_dict[key][1].append(timestamp)

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_dict:
            return ""
        values, timestamps = self.timestamp_dict[key]
        index = self.binary_search(timestamps=timestamps, threshold=timestamp)
        if index == -1:
            return ""
        return values[index]

        
