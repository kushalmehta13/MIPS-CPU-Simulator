#!/usr/bin/env python
class Register:
    def __init__(self, path):
        self.register = dict()
        self.load_init(path)
    def load_init(self, path):
        i = 0
        with open(path) as inp:
            for line in inp:
                self.register['R'+str(i)] = line.strip()
                i+=1
    def get(self, reg):
        if reg < 'R32':
            return self.register[reg]
    def showRegister(self):
        print(self.register)

