class Array:

    def __init__(self, initialSize):
        self.array = [None] * initialSize
        self.nItems = 0

    def __len__(self):
        return self.nItems

    def __getitem__(self, pos):
        if 0 <= pos < self.nItems:
            return self.array[pos]

        return None

    def set_item(self, n, pos: int):
        if 0 <= pos < self.nItems:
            self.array[pos] = n
            return True

        return False

    def insert(self, item):
        self.array[self.nItems] = item
        self.nItems += 1

    def find(self, n):
        for j in range(self.nItems):
            if self.array[j] == n:
                return j

        return -1

    def search(self, item):
        return self[self.find(item)]

    def delete(self, item):
        for j in range(self.nItems):
            if self.array[j] == item:
                self.nItems -= 1
                for k in range(j, self.nItems):
                    self.array[k] = self.array[k+1]

                return True

        return False

    def traverse(self, function=print):
        for j in range(self.nItems):
            function(self.array[j])
