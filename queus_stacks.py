# Queues are FIFO or First In First Out
# # void enq(item) add item to the end of the queue
# item deq() return the item @ begining of the queue and remove it
# item front() item tail() returning (but not removing) items at the front and back of the queue
# void clear() removes all items.
# API = Application Programm's interface
# Stacks: Last In First Out
# Push = add on item to top of stack (void push(item))
# Pop = return item on top and removes it (item-pop() change the stack and data structure)
# Peek = return item on top of stack (item-peak()-only looks at the stack but doesn't change it.)
# is_empty = t/f whether the stack contains elements
# Clear - removes all items (void clear() it just clears it all)
# e,v,e  e = e,v false e, v, e .  e, =e, e, v, e, r, y
# d, r, deq=d, r, h, y deq=r, h, y, i, a false h
import os


class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    stack = Stack()
