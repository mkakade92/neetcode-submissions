class TimeMap:

    def __init__(self):
        self.mp ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.mp:
            self.mp[key] = [[value,timestamp]]
        else:
            self.mp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mp:
            return ""
        
        values = self.mp[key]

        st = 0
        en = len(values)-1
        while st<=en:
            mid = (st+en)//2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                st = mid+1
            else:
                en = mid-1
        
        if en>=0:
            return values[en][0]
        return ""

        
