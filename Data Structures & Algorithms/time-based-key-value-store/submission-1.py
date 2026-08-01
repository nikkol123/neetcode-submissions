from collections import defaultdict
class TimeMap:

    def __init__(self):
        #key - name
        #value - [timestamp, value]
        self.d = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
        print(self.d)

    def get(self, key: str, timestamp: int) -> str:
        for time, val in reversed(self.d[key]):
            if time <= timestamp: return val
        return ""
