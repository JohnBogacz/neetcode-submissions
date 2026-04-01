class MinStack:

    def __init__(self):
        self.s = list()
        self.m = list()

    def push(self, val: int) -> None:
        self.s.append(val)

        if len(self.m) == 0:
            self.m.append(val)
        else:
            self.m.append(
                min(val, self.m[-1])
            )

    def pop(self) -> None:
        self.m.pop()
        return self.s.pop()


    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
