import processor as pr
import json


INIT_CAP = 10000

if __name__ == '__main__':
    proc = pr.Processor()
    proc.add_tank('Input', 10, 10, INIT_CAP)

    with open('data.json', 'r') as filename:
        data = json.load(filename)

    tanks = data['tanks']
    flows = data['flows']
    proc.add_tank_list(tanks)
    proc.add_flow_list(flows)
    proc.start(True)
