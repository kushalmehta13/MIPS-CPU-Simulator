class MemoryUnit:
    def __init__(self, accessTime):
        self.accessTime = accessTime

    def getAccessTime(self):
        return self.accessTime

    def showInfo(self):
        print('Access Time:', self.accessTime)
        print()