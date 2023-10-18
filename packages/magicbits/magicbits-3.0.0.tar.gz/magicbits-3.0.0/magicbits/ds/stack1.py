# Stack ADT
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def __repr__(self) -> str:
        return f'Stack({self.items})'


if __name__ == '__main__':
    s=Stack()
    print('Stack operation examples')
    s.push(15)
    s.push(20)
    print("Pointer At:", s.peek())

    print(f"{s} size: {s.size()}")
    print("Item Popped:", s.pop())
    print("Item Popped:", s.pop())
    print("Size of Stack", s.size())
    print('Is Stack Empty:', s.isEmpty())

