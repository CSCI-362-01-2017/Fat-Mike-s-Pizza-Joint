class testObject:
    def __init__(self, casePath):
        self.caseSource = open(casePath, "r")
    
    def printSource(self):
        print(self.caseSource)
