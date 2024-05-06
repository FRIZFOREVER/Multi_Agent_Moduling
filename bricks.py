class Tank:
    def __init__(self, name, x, y, contains=10000):
        self.container = contains
        self.name = name
        self.x = x
        self.y = y

    def current_capacity(self):
        return self.container

    def draw_amount(self, amount):
        if self.container - amount > 0:
            drew = amount
            self.container -= amount
        else:
            drew = self.container
            self.container = 0
        return drew

    def add_amount(self, amount):
        self.container += amount

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return (f' {self.name} contains {self.container} ')


class Flow:
    def __init__(self, pace, target, receiver):
        self.pace = pace
        self.target = target
        self.receiver = receiver

    def update(self):
        drew = self.target.draw_amount(self.pace)
        self.receiver.add_amount(drew)

    def __str__(self):
        return (f' from {self.target} going to'
                + f'{self.receiver} with {self.pace} ')
