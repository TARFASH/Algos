import random

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
        return 10**18


    def clear(self):
        self.arr = []
        return "ok"

class StackMin:
    def __init__(self):
        self.stack = Stack()
        self.stack_min = Stack()

    def push(self, n):
        self.stack.push(n)
        if self.stack_min.size():
            self.stack_min.push(min(n, self.stack_min.back()))  # 🔧 ИЗМЕНЕНО: минимумы поддерживаем правильно
        else:
            self.stack_min.push(n)

    def min(self):
        return self.stack_min.back()

    def pop(self):
        self.stack_min.pop()
        return self.stack.pop()

    def size(self):
        return self.stack.size()


class QueueMin:
    def __init__(self):
        self.push_minstack = StackMin()
        self.pop_minstack = StackMin()

    def push(self, n):
        self.push_minstack.push(n)

    def fill_pop(self):
        while self.push_minstack.size():
            val = self.push_minstack.pop()
            self.pop_minstack.push(val)
        # 🔧 УДАЛЕНО: лишнее копирование массива минимумов (сломает структуру)

    def pop(self):
        if not self.pop_minstack.size():
            self.fill_pop()
        return self.pop_minstack.pop()

    def get_min(self):
        if self.push_minstack.size() and self.pop_minstack.size():
            return min(self.push_minstack.min(), self.pop_minstack.min())
        elif self.push_minstack.size():
            return self.push_minstack.min()
        elif self.pop_minstack.size():
            return self.pop_minstack.min()
        else:
            return 10**18  # ИЗМЕНЕНО: добавлена защита от пустой очереди

    def size(self):
        return self.push_minstack.size() + self.pop_minstack.size()


def min_in_sliding_window(sequence, k):
    q = QueueMin()
    res = []

    for i in range(len(sequence)):
        q.push(sequence[i])
        if q.size() > k:
            q.pop()
        if q.size() == k:
            res.append(q.get_min())

    return res


# пример использования:
if __name__ == "__main__":
    # ИЗМЕНЕНО: подключено чтение данных как в задаче
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    result = min_in_sliding_window(sequence, K)
    print("\n".join(map(str, result)))