import bricks


class Processor:
    flows = []
    tanks = {}
    running = False

    def __init__(self, speed=1):
        self.speed = speed

    def add_tank(self, name, initial_cap=0):
        tank = bricks.Tank(name, initial_cap)
        self.tanks[name] = tank

    def add_flow(self, target, receiver, pace=1):
        flow = bricks.Flow(pace, target, receiver)
        self.flows.append(flow)

    def start(self):
        self.running = True
        pass

    def update_system(self):
        for _ in range(self.speed):
            (flow.update() for flow in self.flows)

    def run_check(self):
        if self.running:
            raise Exception('Model is running')


if __name__ == '__main__':
    process = Processor()
    process.start()
    process.add_tank('Test')
