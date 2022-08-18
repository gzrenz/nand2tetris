from ParserC import Parser

import Code 
import sys 

class Assembler: 
    symbolDict = {} 

    def __init__(self, dir): 
        # initialize file and writer objects 
        self.path = str(dir) 
        

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

        self.run() 

        return 

    def run(self): 
        # first pass  
        self.firstPass() 
        self.secondPass() 

        # terminate 
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

    # Helper method for converting int to binary values 
    def binary(self, num): 
        result = bin(num)[2:].zfill(16)
        return result 

    # Maps the asm labels to hack ROM address - handles pseudo instructions 
    def firstPass(self): 
        lineNum = -1 
        reader = open(self.path)
        parser = Parser(reader)
        while True: 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 
            parser.instructionType() 
            lineNum += 1 
            if parser.instType == 'L_INSTRUCTION':
                if lineNum < 1000: 
                    print(f"Symbol: {parser.symbol()} Line: {lineNum}")
                    print(lineNum)
                self.addEntry(parser.symbol(), lineNum) 
                # Label isn't part of hack code, so don't map a line number. This makes the added entry point to the next instruction. 
                lineNum -= 1 
        reader.close() 
            

    # Maps asm variables to hack RAM address - code generation 
    def secondPass(self): 
        # Create parser to go through each line 
        reader = open(self.path)
        parser = Parser(reader)
        writer = open(f'{self.path[:len(self.path)-4]}.hack', 'w')
        # Start variable mapping at address 16 
        addr = 16
        while True: 
            # Iterate through the asm program until no more lines 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 
            parser.instructionType() 
            it = parser.instType
            # Skip labels (done in first pass) 
            if it == 'L_INSTRUCTION': 
                pass 
            # Parse and code address instructions 
            elif it == 'A_INSTRUCTION': 
                # Get digits or characters after @ 
                s = parser.symbol() 

                # Handling constants - s is string of int 
                if s.isnumeric(): 
                    writer.write(self.binary(int(s)))
                    writer.write('\n')
                # Handling variables - s is string key 
                else: 
                    if self.contains(s): 
                        writer.write(self.binary(int(self.symbolDict[s]))) 
                        writer.write('\n')
                    # Map new variables - s is key and addr is value 
                    else: 
                        self.symbolDict[s] = addr 
                        addr += 1 
                        writer.write(self.binary(int(self.symbolDict[s])))
                        writer.write('\n')
            # currentline is C_INSTRUCTION
            else: 
                writer.write('111')
                destSymbol = parser.dest() 
                compSymbol = parser.comp() 
                jumpSymbol = parser.jump() 

                writer.write(Code.comp(compSymbol)) 
                writer.write(Code.dest(destSymbol))
                writer.write(Code.jump(jumpSymbol)) 
                writer.write('\n') 
        reader.close() 
        writer.close() 
        return 

if __name__ == '__main__':
    dir = sys.argv[1] 
    Assembler(dir)  
