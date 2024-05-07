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
    def __init__(self, pace, target, receiver, anch_srt='e', anch_end='w'):
        self.pace = pace
        self.target = target
        self.receiver = receiver
        self.anch_srt = anch_srt
        self.anch_end = anch_end

    def update(self):
        drew = self.target.draw_amount(self.pace)
        self.receiver.add_amount(drew)

    def __str__(self):
        return (f' from {self.target} going to'
                + f'{self.receiver} with {self.pace} ')

    def get_start(self):
        x, y = self.target.get_coords()
        return {
            self.anch_srt == 'e': [x+100, y+50],
            self.anch_srt == 's': [x+50, y+100],
            self.anch_srt == 'w': [x, y+50],
            self.anch_srt == 'n': [x+50, y],
            self.anch_srt == 'ws': [x, y+100]
        }[True]

    def get_end(self):
        x, y = self.receiver.get_coords()
        return {
            self.anch_end == 'e': [x+100, y+50],
            self.anch_end == 's': [x+50, y+100],
            self.anch_end == 'w': [x, y+50],
            self.anch_end == 'n': [x+50, y],
            self.anch_end == 'ne': [x+100, y]
        }[True]
