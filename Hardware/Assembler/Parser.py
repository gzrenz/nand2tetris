from dis import Instruction
import re 
class Parser: 
    """Parses the input into instructions and instructions into fields"""

    # Attributes 
    currentline = '' 
    instructionType = ''
    labelPattern = re.compile(r'\((\w)*\)')
    addressPattern = re.compile(r'@(\w)*|@(\d)*')
    compPattern = re.compile(r'0|1|D|M')

    def __init__(self, file):
        self.file = open(file) 
        return 

    # Checks if next line in file isn't empty
    def hasMoreLines(self): 
        pos = self.file.tell() 
        line = self.file.readline()
        if line: 
            self.file.seek(pos) 
            return True 
        else: 
            return False 

    # advances 
    def advance(self): 
        line = self.file.readline() 
        if "//" in line: 
            tokens = line.split('//') 
            if tokens[0] == '': 
                if self.hasMoreLines: 
                    self.advance() 
            else: 
                if re.search('\W', tokens[0]): 
                    self.advance() 
                else:
                    self.currentline = tokens[0]
        elif re.search('\W', line): 
            self.advance() 
        else: 
            self.currentline = line 
            
    # Return C_INSTRUCTION if comp, 
    def instructionType(self): 
        if self.labelPattern.search(self.currentline): 
            self.instructionType = 'L_INSTRUCTION'
        elif self.addressPattern.search(self.currentline): 
            self.instructionType = 'A_INSTRUCTION'
        elif self.compPattern.search(self.currentline): 
            self.instructionType = 'C_INSTRUCTION' 
        else: 
            print('Instruction is undefined')

    def symbol(self):
        return re.search('(\w)*', self.currentline).group()

    def dest(): 
        return 

    def comp(): 
        return 

    def jump(): 
        return 