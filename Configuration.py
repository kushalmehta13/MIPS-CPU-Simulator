#!/usr/bin/env python
from ExecutionUnit import ExecutionUnit
from MemoryUnit import MemoryUnit
class Config:
    def __init__(self, path):
        self.configure(path)
        self.IntUnit = ExecutionUnit(1, True)

    def configure(self, path):
        with open(path) as inp:
            for line in inp:
                line = line.strip()
                # if the line read has FP, initialize all the floating point FU's
                if line.split(' ')[0] == 'FP':
                    unit = line.split(' ')[1].lower().strip(':')
                    count, pipelined = self.parseString(line.split(':')[1])
                    if unit == 'adder':
                        self.FPAdder = ExecutionUnit(count, pipelined)
                    if unit == 'multiplier':
                        self.FPMult = ExecutionUnit(count, pipelined)
                    if unit == 'divider':
                        self.FPDiv = ExecutionUnit(count, pipelined)

                # Else if the line read is Main Memory, initialize the access time for main memory
                else:
                    access_time = int(line.split(':')[1].split(' ')[1])
                    unit = line.split(' ')[0].lower().strip(':')
                    if unit == 'main':
                        self.MainMem = MemoryUnit(access_time)
                    if unit == 'i-cache':
                        self.ICache = MemoryUnit(access_time)
                    if unit == 'd-cache':
                        self.DCache = MemoryUnit(access_time)


    def getFPAdder(self):
        return self.FPAdder

    def getFPMult(self):
        return self.FPMult

    def getFPDiv(self):
        return self.FPDiv

    def getMainMem(self):
        return self.MainMem

    def getICache(self):
        return self.ICache

    def getDCache(self):
        return self.DCache

    def getIntUnit(self):
        return self.IntUnit

    def parseString(self, s):
        lookup = {' yes': True, ' no': False}
        return int(s.split(',')[0]), lookup[s.split(',')[1]]

    def showConfigs(self):
        print('Integer Unit')
        print('-----------')
        self.getIntUnit().showInfo()
        print('FP Adder')
        print('-----------')
        self.getFPAdder().showInfo()
        print('FP Multiplier')
        print('-----------')
        self.getFPMult().showInfo()
        print('FP Divider')
        print('-----------')
        self.getFPDiv().showInfo()
        print('Main Memory')
        print('-----------')
        self.getMainMem().showInfo()
        print('I-Cache')
        print('-----------')
        self.getICache().showInfo()
        print('D-Cache')
        print('-----------')
        self.getDCache().showInfo()