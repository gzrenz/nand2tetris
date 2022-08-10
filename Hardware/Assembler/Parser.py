
class Parser: 
    """Parses the input into instructions and instructions into fields"""

    # Attributes 
    currentline = '' 

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


    def advance(self): 
        line = self.file.readline() 
        tokens = line.split('//') 
        if len(tokens) == 0: 
            currentline = ''
        else: 
            currentline = tokens[0]

    def instructionType(): 
        return 

    def symbol(): 
        return 

    def dest(): 
        return 

    def comp(): 
        return 

    def jump(): 
        return 