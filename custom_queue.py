from typing import List
from typing import TypeVar, Generic

T = TypeVar('T')


class CustomQueue(Generic[T]):
    queue: List[T]

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if value:
            self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def first_element(self):
        if len(self.queue) > 0:
            return self.queue[0]
