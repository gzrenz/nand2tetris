# If M in instruction, use dict1
# else use dict0 
c_dict0 = {
    '0'  : '0101010', 
    '1'  : '0111111', 
    '-1' : '0111010', 
    'D'  : '0001100', 
    'A'  : '0110000', 
    '!D' : '0001101', 
    '!A' : '0110001', 
    '-D' : '0001111', 
    '-A' : '0110011', 
    'D+1': '0011111', 
    'A+1': '0110111', 
    'D-1': '0001110', 
    'A-1': '0110010', 
    'D+A': '0000010', 
    'D-A': '0010011', 
    'A-D': '0000111', 
    'D&A': '0000000', 
    'D|A': '0010101', 
}
c_dict1 = {
    '0'  : '1101010', 
    '1'  : '1111111', 
    '-1' : '1111010', 
    'D'  : '1001100', 
    'M'  : '1110000', 
    '!D' : '1001101', 
    '!M' : '1110001', 
    '-D' : '1001111', 
    '-M' : '1110011', 
    'D+1': '1011111', 
    'M+1': '1110111', 
    'D-1': '1001110', 
    'M-1': '1110010', 
    'D+M': '1000010', 
    'D-M': '1010011', 
    'M-D': '1000111', 
    'D&M': '1000000', 
    'D|M': '1010101',
}
d_dict = { 
    None : '000',
    'M'  : '001',
    'A'  : '100', 
    'D'  : '010', 
    'AM' : '101', 
    'DM' : '011', 
    'AD' : '110', 
    'ADM': '111', 
    'MD' : '011'
}
j_dict = { 
    None : '000',
    'JMP': '111', 
    'JGT': '001', 
    'JLT': '100', 
    'JEQ': '010', 
    'JGE': '011', 
    'JLE': '110', 
    'JNE': '101' 
}

# Return binary string for C_INSTRUCTION
def dest(symbol):
    # print(f"Symbol: {symbol}, Value: {d_dict[symbol]}")
    return d_dict[symbol]

def comp(symbol): 
    if 'M' in symbol: 
        # print(f"Symbol: {symbol}, Value: {c_dict1[symbol]}")
        return c_dict1[symbol] 
    else: 
        # print(f"Symbol: {symbol}, Value: {c_dict0[symbol]}")
        return c_dict0[symbol] 

def jump(symbol): 
    # print(f"Symbol: {symbol}, Value: {j_dict[symbol]}")
    return j_dict[symbol]