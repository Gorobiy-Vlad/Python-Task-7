class Iterator:
    limit = 0
    val = 0
    Fibonacci = [1, 1]

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.val = 1
        print("Create Iterator:")
        print(f"Start {self.val} -->{self.Fibonacci}")
        return self

    def __next__(self):
        if self.val == self.limit:
            raise StopIteration
        self.Fibonacci.append(self.Fibonacci[self.val] + self.Fibonacci[self.val - 1])
        self.val += 1
        return f"Next  {self.val} -->{self.Fibonacci}"
