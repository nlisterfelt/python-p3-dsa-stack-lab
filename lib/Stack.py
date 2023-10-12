class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.full():
            return None
        else:
            self.items.append(item)

    def pop(self):
        num = len(self.items)-1
        if num>=0:
            popped = self.items[num]
            del self.items[num]
            return popped
        else: 
            return None

    def peek(self):
        num = len(self.items)
        return self.items[num-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        i = len(self.items)-1
        while i>=0:
            if self.items[i] == target:
                return len(self.items) - i - 1
            else:
                i -= 1
        return -1
