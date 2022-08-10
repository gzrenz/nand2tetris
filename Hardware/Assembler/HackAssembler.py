from Parser import Parser

class Assembler: 
    symbolDict = {} 
    lineNum = -1 

    def __init__(self, dir): 
        # initialize file and writer objects 
        self.file = open(dir)
        self.writer = open(f'{dir[:len(dir)-4]}.hack', 'w')

        # initialize symbol table / dictionary 
        for i in range(16): 
            self.symbolDict[f'R{i}'] = i
        self.symbolDict['SP'] = 0
        self.symbolDict['LCL'] = 1
        self.symbolDict['ARG'] = 2
        self.symbolDict['THIS'] = 3
        self.symbolDict['THAT'] = 4
        self.symbolDict['SCREEN'] = 16384
        self.symbolDict['KBD'] = 24576

        # first pass  
        self.firstPass() 
        self.secondPass() 

        # terminate 
        print("Compilation Finished")
        return 
    
    def addEntry(): 
        """Adds <symbol, address>"""
        return 

    def contains(): 
        """Does the symbol table contain the given symbol?"""
        return 

    def getAddress(): 
        """Returns the address associated with the symbol"""
        return 

    def stringToBits(): 
        return 

    # Maps the asm labels to hack ROM address 
    def firstPass(self): 
        parser = Parser(self.file)
        while True: 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 
            if parser.instructionType() == 'L_INSTRUCTION':
                self.symbolDict[parser.symbol()] = self.lineNum + 1
            lineNum += 1 

    def secondPass(): 
        parser = Parser(self.file)
        return 

if '__main__' == __name__:
    print 
