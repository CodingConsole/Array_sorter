import random 

class generator:
    def __init__(self):
        self.field = list()
        pass

    def generate(self):
        self.field.clear()
        for x in range(100):
            self.field.append(random.randint(0, 1000))

    def sort_1(self):
        self.sorted = self.field
        for x in range(100):
            for y in range(x + 1, 100):
                if (self.sorted[x] > self.sorted[y]):
                    cache = self.sorted[x]
                    self.sorted[x] = self.sorted[y]
                    self.sorted[y] = cache    
        pass
