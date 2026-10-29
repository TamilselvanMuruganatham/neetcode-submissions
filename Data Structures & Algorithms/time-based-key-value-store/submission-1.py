class TimeMap:

    def __init__(self):
        self.store=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        array=self.store.get(key,[])
        if not array:
            return ''
        l=0
        r=len(array)-1
        while l<=r:
            mid=(l+r)//2
            mid_value,mid_timestamp=array[mid]
            if mid_timestamp==timestamp:
                return mid_value
            if mid_timestamp>timestamp:
                r=mid-1
            else:
                l=mid+1
        if r>=0:
            return array[r][0]

        return ''

            
        
