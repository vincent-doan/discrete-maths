class queue:
    def __init__(self):
        self.queue = list()
    def __len__(self):
        return len(self.queue)
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue(self, item):
        self.queue.append(item)

class stack:
    def __init__(self):
        self.stack = list()
    def __len__(self):
        return len(self.stack)
    def pop(self):
        return self.stack.pop(0)
    def push(self, item):
        self.stack = [item] + self.stack

class priorityqueue:
    def __init__(self):
        self.priorityqueue = list()
        self.min = min
    def __len__(self):
        return len(self.priorityqueue)
    def dequeue(self):
        min_weight = None
        min_index = None
        for (index, (_, weight)) in enumerate(self.priorityqueue):
            if min_weight == None or min_weight > weight:
                min_weight = weight
                min_index = index
        return self.priorityqueue.pop(min_index)
    def enqueue(self, item: tuple):
        self.priorityqueue.append(item)