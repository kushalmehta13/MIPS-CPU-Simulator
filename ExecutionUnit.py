class ExecutionUnit:
    def __init__(self, count, pipelined):
        self.cycleCount = count
        self.Pipelined = pipelined

    def getCycleCount(self):
        return self.cycleCount

    def isPipelined(self):
        return self.Pipelined

    def showInfo(self):
        print('Cycles:', self.cycleCount)
        print('Is Pipelined:', self.Pipelined)
        print()