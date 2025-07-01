class Stack:
    def __init__(self):
        self.arr = []

    def push(self, n):
        self.arr.append(n)
        return "ok"

    def size(self):
        return len(self.arr)

    def pop(self):
        if self.size():
            return self.arr.pop()
        return "error"

    def back(self):
        if self.size():
            return self.arr[-1]
        return "error"

    def clear(self):
        self.arr = []
        return "ok"

    def exit(self):
        return "bye"

    def str_call(self, string:str):
        parts = string.strip().split()
        if len(parts) > 1:
            return self.push(int(parts[1]))
        funcs = {
            "size": self.size,
            "pop": self.pop,
            "back": self.back,
            "clear": self.clear,
            "exit": self.exit
        }
        return funcs[parts[0]]()


stack = Stack()

while True:
    result = stack.str_call(input())
    print(result)
    if result == "bye":
        break