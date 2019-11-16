class Instruction:
    def __init__(self, inst):
        self.inst = inst
        self.instType = ''
        self.op1 = ''
        self.op2
        self.op3 = ''
        self.offset = 0

    def setOp1(self, op1):
        self.op1 = op1

    def setOp2(self, op2):
        self.op2 = op2

    def setOp3(self, op3):
        self.op3 = op3

    def setOffset(self, offset):
        self.offset = offset

    def setInstType(self, instType):
        self.instType = instType

    def getOp1(self, op1):
        return self.op1

    def getOp2(self, op2):
        return self.op2

    def getOp3(self, op3):
        return self.op3

    def getOffset(self, offset):
        return self.offset

    def getInstType(self, instType):
        return self.instType