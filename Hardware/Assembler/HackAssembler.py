from ParserC import Parser

import Code 
import sys 

class Assembler: 
    symbolDict = {} 

    def __init__(self, dir): 
        # initialize file and writer objects 
        path = str(dir) 
        self.file = open(path)
        self.writer = open(f'{path[:len(path)-4]}.hack', 'w')

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
        return 

    def run(self): 
        # first pass  
        self.firstPass() 
        self.secondPass() 

        # terminate 
        self.writer.close() 
        print("Compilation Finished")
        return 
    
    def addEntry(self, symbol, address): 
        """Adds <symbol, address>"""
        self.symbolDict[symbol] = address 
        return 

    def contains(self, symbol): 
        """Does the symbol table contain the given symbol?"""
        return symbol in self.symbolDict

    def getAddress(self, symbol): 
        """Returns the address associated with the symbol"""
        return self.symbolDict[symbol]

    # Convenient method for line breaks 
    def newLine(self): 
        self.writer.write('\n')
        return 

    # Maps the asm labels to hack ROM address - handles pseudo instructions 
    def firstPass(self): 
        lineNum = -1 
        parser = Parser(self.file)
        while True: 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 
            if parser.instructionType() == 'L_INSTRUCTION':
                self.symbolDict[parser.symbol()] = self.lineNum + 1
            lineNum += 1 

    # Maps asm variables to hack RAM address - code generation 
    def secondPass(self): 
        # Create parser to go through each line 
        parser = Parser(self.file)
        # Start variable mapping at address 16 
        addr = 16
        i = 0
        while True: 
            print(++i)
            # Iterate through the asm program until no more lines 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 

            it = parser.instructionType() 
            # Skip labels (done in first pass) 
            if it == 'L_INSTRUCTION': 
                pass 
            # Parse and code address instructions 
            elif it == 'A_INSTRUCTION': 
                # Get digits or characters after @ 
                s = parser.symbol() 

                # Handling constants - s is string of int 
                if isinstance(s, int): 
                    self.writer.write(bin(int(s)))
                    self.newLine() 
                # Handling variables - s is string key 
                else: 
                    if s in self.symbolDict: 
                        self.writer.write(bin(int(self.symbolDict[s]))) 
                        self.newLine() 
                    # Map new variables - s is key and addr is value 
                    else: 
                        self.symbolDict[s] = addr 
                        ++addr 
                        self.writer.write(bin(int(self.symbolDict[s])))
                        self.newLine() 
            # currentline is C_INSTRUCTION
            else: 
                destSymbol = parser.dest() 
                compSymbol = parser.comp() 
                jumpSymbol = parser.jump() 

                self.writer.write(Code.dest(destSymbol))
                self.writer.write(Code.comp(compSymbol)) 
                self.writer.write(Code.jump(jumpSymbol)) 
                self.newLine() 
        return 

if __name__ == '__main__':
    dir = sys.argv[1] 
    Assembler(dir)  
