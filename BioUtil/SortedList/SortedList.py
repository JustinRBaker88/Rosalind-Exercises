import bisect

class SortedList(object):

    _sortedList = []

    def __init__(self, data = None):
        self._sortedList = []
        if (data is not None):
            if (type(data) is int):
                self.insert(data)
            else:
                for values in data:
                    self.insert(values)
    
    def __iter__(self):
        return iter(self._sortedList)
    
    def __getitem__(self, key):
        return self._sortedList[key]
    
    def size(self) -> int:
        return len(self._sortedList)
    
    def insert(self, value: int):
        bisect.insort(self._sortedList, value)
    
    def remove(self, value: int):
        del self._sortedList[bisect.bisect_left(self._sortedList, value)]
    
    def getLargestValue(self):
        return self._sortedList[self.size() - 1]
    
    def getSmallestValue(self):
        return self._sortedList[0]
    
    def __contains__(self, key):
        return key in self._sortedList
    
    def contains(self, value):
        return value in self._sortedList
    
    def __str__(self):
        return str(self._sortedList)