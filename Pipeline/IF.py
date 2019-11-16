from Memory import Memory
from Operands import Ops

class InstructionFetch:
    # Input: Memory Address
    # Operation: Lookup Address and fetch instruction
    # Output: Parsed instructions
    def __init__(self, inst_addr, memory):
        # The number of cycles that IF will run for assuming cache hit
        self.counter = 3
        self.memory = memory
        self.instruction = self.memory.get_instruction(inst_addr)
        self.busy = True
        self.ops = Ops()
        self.parse()

    def isBusy(self):
        return self.busy

    def updateCounter(self):
        if self.counter > 1:
            self.counter -= 1
        else:
            self.counter = 3
            self.busy = False

    def fetch(self, inst_addr):
        self.instruction = self.memory.get_instruction(inst_addr)
        self.busy = True
        self.parse()
        # if self.hasWAW() == False:
        #     self.run()

    def parse(self):
        self.instructionSplit = self.instruction.split()
        self.ops.InstType = self.instructionSplit[0]
        # opsSplit = self.instructionSplit[1].split(',')
        if self.ops.InstType in ['LW', 'L.D']:
            self.ops.dest = self.instructionSplit[1]
            self.ops.s1 = self.instructionSplit[2]
        if self.ops.InstType in ['SW', 'S.D']:
            self.ops.dest = self.instructionSplit[1]
            self.ops.s1 = self.instructionSplit[2]
        print('Instruction Type:',self.ops.InstType)
        print('Source1:', self.ops.s1)
        print('Source2:', self.ops.s2)
        print('Destination:', self.ops.dest)