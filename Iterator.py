class MyIterator:
    "My first iterator"

    def __init__(self, start, end):
        self.start, self.end = start - 1, end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start


for item in MyIterator(1, 10):
    print(item)