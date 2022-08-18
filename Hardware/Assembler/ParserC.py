from dis import Instruction
import re
import string 
class Parser: 
    """Parses the input into instructions and instructions into fields"""

    # Attributes 
    currentline = '' 
    instType = ''
    lines = []
    labelPattern = re.compile(r'\(\w+\W\w+\W\w+\)|\(\w+.\w+\)|\((\w)+\)')
    addressPattern = re.compile(r'@w+.w+|@\w+|@\d+')
    compPattern = re.compile(r'0|1|D|M')
    ws = re.compile(r'\s+')

    def __init__(self, file):
        self.lines = file.readlines() 
        # Remove whitespace and comments 
        for i, line in enumerate(self.lines): 
            if '//' in line: 
                line = line.split('//', 1)[0] 
            line = re.sub(self.ws, '', line)
            self.lines[i] = line
            
        # Remove empty strings from queue 
        while("" in self.lines): 
            self.lines.remove("") 
        return 

    # Checks if next line in file isn't empty
    def hasMoreLines(self): 
        if not self.lines: 
            return False 
        else: 
            return True 

    # advances 
    def advance(self): 
        line = self.lines.pop(0) 
        self.currentline = line 
            
    # Return instruction type  
    def instructionType(self): 
        if self.labelPattern.search(self.currentline): 
            self.instType = 'L_INSTRUCTION'
        elif self.addressPattern.search(self.currentline): 
            self.instType = 'A_INSTRUCTION'
        elif self.compPattern.search(self.currentline): 
            self.instType = 'C_INSTRUCTION'
        else: 
            print(self.instType)
            print('Instruction is undefined')

    def symbol(self):
        """Return string for labels and address and int for constants. 
            Exclusive for Addr and Label instructions"""
        return re.search('\w+\W\w+\W\w+|\w+.\w+|\w+|\d+', self.currentline).group()
        
       


    # For parsing dest = comp ; jump instructions 
    # comp is mandatory 
    # if dest is empty, '=' isn't included in asm program
    # ^-^jump^--------^,';' ^----------------------------^
    def dest(self): 
        parsed = self.currentline.split('=') 
        if len(parsed) > 1: 
            parsed = parsed[0]
            #remove whitespace and return
            return re.sub(self.ws, "", parsed)
        else: 
            return None

    def comp(self): 
        parsed = ''
        if '=' in self.currentline: 
            parsed = self.currentline.split('=')[1].strip()
        else: # ';' in inst 
            parsed = self.currentline.split(';')[0].strip() 
        return re.sub(self.ws, "", parsed)

    def jump(self):  
        parsed = self.currentline.split(';')
        if len(parsed) > 1: 
            parsed = parsed[1]
            return re.sub(self.ws, "", parsed)
        else: 
            return None 