class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Bucket(0)  # sentinel, count is meaningless
        self.tail = Bucket(0)  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyCount = {}  # key -> Bucket

    def _insert_after(self, node, new_bucket):
        """Insert new_bucket right after node."""
        new_bucket.prev = node
        new_bucket.next = node.next
        node.next.prev = new_bucket
        node.next = new_bucket

    def _remove(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key: str) -> None:
        if key not in self.keyCount:
            if self.head.next.count == 1:
                target = self.head.next
            else:
                target = Bucket(1)
                self._insert_after(self.head, target)
            target.keys.add(key)
            self.keyCount[key] = target
        else:
            bucket = self.keyCount[key]
            newCount = bucket.count + 1
            
            if bucket.next.count == newCount:
                target = bucket.next
            else:
                target = Bucket(newCount)
                self._insert_after(bucket, target)
            
            target.keys.add(key)
            self.keyCount[key] = target
            
            bucket.keys.remove(key)
            if not bucket.keys:
                self._remove(bucket)

    def dec(self, key: str) -> None:
        bucket = self.keyCount[key]
        
        if bucket.count == 1:
            del self.keyCount[key]
        else:
            newCount = bucket.count - 1
            
            if bucket.prev.count == newCount:
                target = bucket.prev
            else:
                target = Bucket(newCount)
                self._insert_after(bucket.prev, target)
            
            target.keys.add(key)
            self.keyCount[key] = target
        
        bucket.keys.remove(key)
        if not bucket.keys:
            self._remove(bucket)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))