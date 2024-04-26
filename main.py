import bricks


class Processor:
    flows = []
    tanks = []

    def hw(self):
        print('Hello, world')

    def __init__(self, speed=1):
        self.speed = 1

    def add_flow(self, tanks, pace=1):
        flow = bricks.Flow(pace, tanks[0], tanks[1])
        self.flows.append(flow)

    def start(self):
        pass

    def update_system(self):
        pass

    def add_tank(self):
        pass


if __name__ == '__main__':
    process = Processor()
    process.hw()
