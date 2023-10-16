class LRUPage:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = []

    def refer(self, page):
        if page in self.cache:
            self.cache.remove(page)
            self.cache.append(page)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(page)

    def display(self):
        for page in self.cache:
            print(page, end=" ")
        print()

if __name__ == '__main__':
    lru_cache = LRUPage(3)

    for i in range(1, 4):
        lru_cache.refer(i)

    print('Current Cache contents:')
    lru_cache.display()
    lru_cache.refer(2)

    print('Updated Cache')
    lru_cache.display()
    lru_cache.refer(4)

    print("Cache contents after page fault:")
    lru_cache.display()