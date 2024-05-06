import processor as pr


INIT_CAP = 10000

if __name__ == '__main__':
    proc = pr.Processor()
    proc.add_tank('Input', 10, 10, INIT_CAP)
    tanks = [
        ['Sorter_Al', 310, 160],
        ['Sorter_Cu', 10, 160],
        ['Disassembler_Al', 460, 160],
        ['Disassembler_Cu', 160, 160],
        ['Output', 460, 460]
    ]
    flows = [
        ['Input', 'Sorter_Al', 2],
        ['Input', 'Sorter_Cu', 2],
        ['Sorter_Al', 'Disassembler_Al', 1.5],
        ['Sorter_Cu', 'Disassembler_Cu', 1.5],
        ['Disassembler_Al', 'Sorter_Cu', 0.2],
        ['Disassembler_Cu', 'Sorter_Al', 0.2],
        ['Disassembler_Al', 'Output', 0.8],
        ['Disassembler_Cu', 'Output', 0.8]
    ]
    for name, x, y in tanks:
        proc.add_tank(name, x, y)
    for target, receiver, pace in flows:
        proc.add_flow(target, receiver, pace)
    [print(item) for item in proc.tanks]
    [print(item) for item in proc.flows]
    proc.start()
