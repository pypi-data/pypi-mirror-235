from queue import Queue

class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_queue = Queue(maxsize=capacity)
        self.page_set = set()
        self.page_hits = 0
        self.page_misses = 0

    def page_fault(self, page):
        if page not in self.page_set:
            self.page_misses += 1
            if self.page_queue.full():
                removed_page = self.page_queue.get()
                self.page_set.remove(removed_page)
            self.page_queue.put(page)
            self.page_set.add(page)
        else:
            self.page_hits += 1

    def get_hit_ratio(self):
        return self.page_hits / (self.page_hits + self.page_misses)

    def get_miss_ratio(self):
        return self.page_misses / (self.page_hits + self.page_misses)

if __name__ == "__main__":
    capacity = 3  # Set the capacity of the memory
    fifo = FIFOPageReplacement(capacity)

    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    for page in pages:
        fifo.page_fault(page)

    hit_ratio = fifo.get_hit_ratio()
    miss_ratio = fifo.get_miss_ratio()

    print(f"Total Page Hits: {fifo.page_hits}")
    print(f"Total Page Misses: {fifo.page_misses}")
    print(f"Page Hit Ratio: {hit_ratio:.2f}")
    print(f"Page Miss Ratio: {miss_ratio:.2f}")
