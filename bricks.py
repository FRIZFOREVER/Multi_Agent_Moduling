class Tank:
    def __init__(self, name, contains=10000):
        self.container = contains
        self.name = name

    def current_capacity(self):
        return self.container

    def draw_amount(self, amount):
        if self.container - amount > 0:
            drew = amount
            self.container - amount
        else:
            drew = self.container
            self.container = 0
        return drew

    def add_amount(self, amount):
        self.container += amount


class Flow:
    def __init__(self, pace, target, receiver):
        self.pace = pace
        self.target = target
        self.receiver = receiver

    def update(self):
        drew = self.target.draw_amount(self.pace)
        self.receiver.add_amount(drew)
