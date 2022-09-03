import re

class Parser: 
    lines = []
    currentInstruction = [] # command arg1 arg2 

    def __init__(self, file): 
        # Parse instructions into a queue
        self.lines = file.readlines() 
        file.close() 
        # Remove comments and get raw instructions 
        for i, line in enumerate(self.lines): 
            if "//" in line: 
                self.lines[i] = line.split("//", 1)[0]
            self.lines[i] = self.lines[i].strip() 
        # Remove blank instructions 
        while("" in self.lines): 
            self.lines.remove("") 
        return 

    def hasMoreLines(self): 
        if self.lines: 
            return True 
        else: 
            return False 

    def advance(self): 
        self.currentInstruction = self.lines[0].split(" ")
        del self.lines[0] 
        return 

    # return C_ARITHMETIC, C_PUSH, C_POP... 
    def commandType(self): 
        instruction = self.command() 
        if "push" == instruction: 
            return "C_PUSH"
        elif "pop" == instruction: 
            return "C_POP" 
        else: 
            return "C_ARITHMETIC"

    # return string 
    def command(self): 
        return self.currentInstruction[0]
    
    # return string 
    def arg1(self): 
        return self.currentInstruction[1]

    # return int 
    def arg2(self): 
        return self.currentInstruction[2]