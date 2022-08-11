# If M in instruction, use dict1
# else use dict0 
c_dict0 = {
    '0'  : '101010', 
    '1'  : '111111', 
    '-1' : '111010', 
    'D'  : '001100', 
    'A'  : '110000', 
    '!D' : '001101', 
    '!A' : '110001', 
    '-D' : '001111', 
    '-A' : '110011', 
    'D+1': '011111', 
    'A+1': '110111', 
    'D-1': '001110', 
    'A-1': '110010', 
    'D+A': '000010', 
    'D-A': '010011', 
    'A-D': '000111', 
    'D&A': '000000', 
    'D|A': '010101', 
}
c_dict1 = {
    'M'  : '110000', 
    '!M' : '110001', 
    '-M' : '110011', 
    'M+1': '110111', 
    'M-1': '110010', 
    'D+M': '000010', 
    'D-M': '010011', 
    'M-D': '000111', 
    'D&M': '000000', 
    'D|M': '010101'
}
d_dict = { 
    None : '000',
    'M'  : '001',
    'A'  : '100', 
    'D'  : '010', 
    'AM' : '101', 
    'DM' : '011', 
    'AD' : '110', 
    'ADM': '111' 
}
j_dict = { 
    None : '000',
    'JMP': '111', 
    'JGT': '001', 
    'JLT': '100', 
    'JEQ': '010', 
    'JQE': '011', 
    'JLE': '110', 
    'JNE': '101' 
}

# Return binary string for C_INSTRUCTION
def dest(symbol):
    return d_dict[symbol]

def comp(symbol, memoryType): 
    if memoryType == 'M': 
        return c_dict1[symbol] 
    else: 
        return c_dict0[symbol] 

def jump(symbol): 
    return j_dict[symbol]