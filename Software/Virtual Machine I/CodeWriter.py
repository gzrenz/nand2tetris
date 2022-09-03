class CodeWriter: 
    writer = object 

    # To do: Create infinite loop within the asm outpuf file 

    def __init__(self, file): 
        self.writer = file
        # SP = 256 
        self.comment("SP=256")
        self.writer.write("@256\nD=A\n@SP\nM=D\n")
        return 

    # command(C_INSTRUCTION) arg1(segment) arg2(num) 

    def writeArithmetic(self, command, arg1="", arg2=0): 
        if command == "add": 
            self.add() 
        return 
    
    def writePushPop(self, command, arg1="", arg2=0): 
        if command == "push": 
            self.push(arg2) 
        elif command == "pop": 
            self.pop() 
        return 

    # finalize file 
    def close(self): 
        self.writer.close() 

    # add the previous two numbers, prev prev stack value + prev value then increment stack pointer 
    def add(self): 
        self.comment("add")
        self.toPrev() 
        self.writer.write("D=M\n")
        self.toPrev() 
        self.writer.write("M=M+D\n")
        self.spp() 
        return 

    def sub(self): 
        self.comment("subtract")
        self.toPrev() 
        self.writer.write("D=M\n")
        self.toPrev() 
        self.writer.write("M=M-D\n")
        self.spp() 
        return 


    # push the indicated value to the top of the stack then increment stack pointer 
    def push(self, arg2): 
        self.writer.write(f"@{arg2}\nD=A\n")
        self.writer.write("@SP\nA=M\nM=D\n")
        self.spp() 
        return 

    # get current value from the top of the stack then put it in the correct memory segment, decrement stack pointer 
    def pop(self): 
        return 

    # Go to the previous memory at stack (starts at 256)
    def toPrev(self): 
        self.writer.write("@SP\nM=M-1\nA=M\n") 
        return 

    # Increment stack pointer value 
    def spp(self): 
        self.writer.write("@SP\nM=M+1\n")
        return 

    # Writing comments unto the asm program 
    def comment(self, comment): 
        self.writer.write(f"//{comment}\n")


