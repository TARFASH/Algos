class Stack:
    def __init__(self):
        self.arr = []

    def push(self, n):
        self.arr.append(n)

    def pop(self):
        return self.arr.pop()

    def back(self):
        return self.arr[-1]

    def clear(self):
        self.arr = []

    def size(self):
        return len(self.arr)


class DoubleStackQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, n):
        self.push_stack.push(n)
        return "ok"

    def fill_pop(self):
        while self.push_stack.size():
            self.pop_stack.push(self.push_stack.pop())

    def pop(self):
        if self.size() == 0:
            return "error"
        if self.pop_stack.size() == 0:
            self.fill_pop()
        return self.pop_stack.pop()

    def front(self):
        if self.size() == 0:
            return "error"
        if self.pop_stack.size() == 0:
            self.fill_pop()
        return self.pop_stack.back()

    def size(self):
        return self.push_stack.size() + self.pop_stack.size()

    def clear(self):
        self.push_stack.clear()
        self.pop_stack.clear()
        return "ok"


queue = DoubleStackQueue()

while True:
    s = input()
    if s.startswith("push"):
        _, num = s.split()
        print(queue.push(int(num)))
    elif s == "pop":
        print(queue.pop())
    elif s == "front":
        print(queue.front())
    elif s == "size":
        print(queue.size())
    elif s == "clear":
        print(queue.clear())
    elif s == "exit":
        print("bye")
        break