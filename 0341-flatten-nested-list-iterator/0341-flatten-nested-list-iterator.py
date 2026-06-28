class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Push in reverse so the first element ends up on top of the stack
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        # By the time next() is called, hasNext() guarantees
        # the top of the stack is a ready-to-return integer
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # Top is a list — unpack it: remove it, and push its
            # contents (in reverse) so they're processed in order
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False