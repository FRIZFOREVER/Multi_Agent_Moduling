import bricks


class Processor:
    def __init__(self, speed=1, tanks={}, flows=[]):
        self.speed = speed
        self.running = False
        self.flows = flows
        self.tanks = tanks

    def add_tank(self, name, initial_cap=0):
        self.run_check()
        tank = bricks.Tank(name, initial_cap)
        self.tanks[name] = tank

    def add_flow(self, target, receiver, pace=1):
        self.run_check()
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
