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
        self.file = file 
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
        self.currentline = self.currentline.strip() 
            
    # Return instruction type  
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
        """Return string for labels and address and int for constants. 
            Exclusive for Addr and Label instructions"""
        return re.search('(\w)*|(\d)*', self.currentline).group()


    # For parsing dest = comp ; jump instructions 
    # comp is mandatory 
    # if dest is empty, '=' isn't included in asm program
    # ^-^jump^--------^,';' ^----------------------------^
    def dest(self): 
        parsed = self.currentline.split('=') 
        if len(parsed) > 1: 
            parsed = parsed[0]
            #remove whitespace and return
            return parsed.replace(re.search('\W', parsed).group(), "")
        else: 
            return None

    def comp(self): 
        parsed = ''
        if '=' in self.currentline: 
            parsed = self.currentline.split('=')[1].strip()
        else: # ';' in inst 
            parsed = self.currentline.split(';')[0].strip() 
        return parsed.replace(re.search('\W', parsed).group(), "")

    def jump(self):  
        parsed = self.currentline.split(';')
        if len(parsed) > 1: 
            parsed = parsed[1]
            return parsed.replace(re.search('\W', parsed).group(), "")
        else: 
            return None 