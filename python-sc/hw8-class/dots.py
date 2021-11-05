class Dots:
    def __init__(self, a, b):
        self.left = min(a, b)
        self.right = max(a, b)

    def __getitem__(self, item):
        if not isinstance(item, slice):
            step = (self.right - self.left) / (item - 1)
            return (self.left + i * step for i in range(item))
        elif item.step:
            step = (self.right - self.left) / (item.step - 1)
            return (self.left + i * step for i in range(item.start or 0, item.stop or item.step))
        else:
            step = (self.right - self.left) / (item.stop - 1)
            return self.left + (item.start or 0) * step

