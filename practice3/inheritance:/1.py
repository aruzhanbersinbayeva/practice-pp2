class Stringhandler():
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())
handler = Stringhandler()
handler.getString() 
handler.printString()