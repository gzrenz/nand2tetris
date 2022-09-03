from Parser import Parser 
from CodeWriter import CodeWriter 

import sys 

class VirtualMachine: 
    sp = 0 
    stack = [] 
    codeWriter = object 
    parser = object 

    def __init__(self, dir):
        self.codeWriter = CodeWriter(open(f"{dir[:len(dir)-3]}.asm", 'w'))
        self.parser = Parser(open(dir, 'r')) 
        self.run() 
        return 

    def run(self): 
        i = 0
        while self.parser.hasMoreLines(): 
            commandType = '' 
            arg1 = '' 
            arg2 = 0 
            # parser must advance first to get current instruction 
            self.parser.advance() 
            # then get the necessary arguments for codewriter 
            commandType = self.parser.commandType() 
            if commandType == 'C_PUSH': 
                arg1 = self.parser.arg1() 
                arg2 = self.parser.arg2() 
                self.codeWriter.writePushPop('push', arg1, arg2) 
            elif commandType == 'C_POP': 
                arg1 = self.parser.arg1() 
                arg2 = self.parser.arg2() 
                self.codeWriter.writeArithmetic('pop', arg1, arg2) 
            elif commandType == 'C_ARITHMETIC': 
                command = self.parser.command() 
                self.codeWriter.writeArithmetic(command) 
            print(f"Instruction complete: {i}")
            i += 1
        self.codeWriter.close() 
        return

    def writeLoop(): 

        return 

if __name__ == '__main__': 
    dir = f"{sys.argv[1]}" 
    vm = VirtualMachine(dir)

