#!/usr/bin/env python
class Memory:
    def __init__(self, inst_path, data_path):
        # 288 is 0x120
        # 0x00 to 0x100 for instructions and 0x100 to 0x120 for data
        self.instructions = dict()
        self.data = dict()

        # Initialize Text and Data Segments
        self.load_init(inst_path, self.instructions, '0x0', '0x100')
        self.load_init(data_path, self.data, '0x100', '0x120')

    def load_init(self, path, segment, start_addr, end_addr):
        addr = start_addr
        with open(path) as inp:
            for line in inp:
                if int(addr, 16) < int(end_addr, 16):
                    segment[addr] = line.strip().upper()
                    addr = hex(int(addr, 16) + 1)
                else:
                    print('Too much data')
                    return

    def get_instruction(self, addr):
        return self.instructions[addr]

    def get_data(self):
        return self.data



#
# if __name__ == '__main__':
#     memory = Memory('inst.txt', 'data.txt')
#     print(memory.get_instructions())
#     print(memory.get_data())
# # instruction = m.address(0x01)