class MyHashSet:
    def __init__(self):
        self.theSet = []
    def add(self, key: int) -> None:
        for i in self.theSet:
            if i == key: return None
        self.theSet.append(key)

    def remove(self, key: int) -> None:
        for i in self.theSet:
            if i == key: self.theSet.remove(key)

    def contains(self, key: int) -> bool:
        for i in self.theSet:
            if i == key: return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)