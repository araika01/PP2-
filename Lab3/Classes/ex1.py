class string:
    def getstring(self):
        self.string = input()
    def __init__(self):
        self.string = ""
    def printstring(self):
        print(self.string.upper())
string = string()
string.getstring()
string.printstring()