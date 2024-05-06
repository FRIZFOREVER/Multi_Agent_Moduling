import bricks
import time
import graphics


class Processor:
    def __init__(self, speed=1, tanks={}, flows=[]):
        self.speed = speed
        self.running = False
        self.flows = flows
        self.tanks = tanks

    def add_tank(self, name, x=0, y=0, initial_cap=0):
        self.run_check()
        tank = bricks.Tank(name, x, y, initial_cap)
        self.tanks[name] = tank

    def add_tank_list(self, tank_list, debug=False):
        self.run_check()
        for name, x, y in tank_list:
            self.add_tank(name, x, y)
        if debug:
            [print(item) for item in self.tanks]

    def add_flow(self, target, receiver, pace=1):
        self.run_check()
        flow = bricks.Flow(pace, self.tanks[target], self.tanks[receiver])
        self.flows.append(flow)

    def add_flow_list(self, flow_list, debug=False):
        self.run_check()
        for target, receiver, pace in flow_list:
            self.add_flow(target, receiver, pace)
        if debug:
            [print(item) for item in self.flows]

    def create_graph_module(self):
        self.graphics = graphics.Graphics(self)

    def system_run(self, debug=False):
        self.graphics.run()
        while (True):
            self.update_system(debug)
            time.sleep(5)

    def start(self, debug=False):
        self.create_graph_module()
        self.running = True
        self.system_run(debug)

    def update_system(self, debug=False):
        for _ in range(self.speed):
            for flow in self.flows:
                flow.update()
                if debug:
                    print(flow)
                    print()
        if debug:
            [print(self.tanks[item]) for item in self.tanks]

    def run_check(self):
        if self.running:
            raise Exception('Model is running')
