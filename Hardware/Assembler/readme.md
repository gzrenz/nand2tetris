# The Hack Assembler 

## Hack Machine Language Specification

This specification is the contract that Hack assemblers must implement. 

### Programs 

**Binary Hack program**: A binary Hack program is a sequence of text lines,
each consisting of sixteen 0 and 1 characters. If the line starts with a 0 , it
represents a binary A-instruction. Otherwise, it represents a binary C-
instruction.

**Assembly Hack program**: An assembly Hack program is a sequence of
text lines, each being an assembly instruction, a label declaration, or a
comment:

### Symbols 

**Predefined symbols**: R0, R1, ... R15 => 0, 1, ... 15 (RAM Address). SP, LCL, ARG, THIS, THAT => 0, 1, 2, 3, 4. SCREEN, KBD => 16384, 24576

**Label symbols**: For each pseudo-instruction (xxx), xxx refers to the ROM holding the next instruction. In an assembly program, the next instruction refers to the line number after the label. 

**Variable symbols**: Any symbol xxx that is not predefined and not defined elsewhere by a label declaration (xxx) is treated as a variable. The first variable is mapped to RAM[16], the second to RAM[17], and so on. 

### Syntax Conventions 

**Symbols**: Sequence of (a-z), (A-Z), (0-9), (_), (.), ($), and (:) that does not begin with (0-9)

**Constants**: May appear only in A-instructions of the form @ xxx. The
constant xxx is a value in the range 0–32767 and is written in decimal
notation.

**White Space**

**Case Conventions**: Assembly mnemonics are in uppercase. Remaining symbols are case-sensitive. The recommended convention is to use uppercase for labels and lowercase for variables. 

## Assembly to Binary Translation 

### Handling Instructions 
For each assembly instruction, the assembler 

* parses the instruction into its underlying fields; 
* for each field, generates the corresponding bit-code. 
* if the instruction contains a symbolic reference, resolves the symbol into its numeric value;
* assembles the resulting binary codes into a string of sixteen 0 and 1 characters; and
* writes the assembled string to the output file. 

### Handling Symbols 
The Hacke assembler is a two-pass assembler that reads the code twice, from start to end. In the first pass, the assembler builds a symbol table, adds all the label symbols to the table, and generates no code. In the second pass, the assembler handles the variables symbols and generates binary code, using the symbol table. 

**Initialization**

**First pass**: keep track of line number. Line starts at 0, and increments whenever an instruction is encountered, but does not increment when label declaration is encountered, instead it maps the label into the symbol (line number + 1). 

**Second pass**: The assembler goes again through the entire program and
parses each line as follows. Each time an A-instruction with a symbolic
reference is encountered, namely, @ xxx, where xxx is a symbol and not a
number, the assembler looks up xxx in the symbol table. If the symbol is
found, the assembler replaces it with its numeric value and completes the
instruction’s translation. If the symbol is not found, then it must represent a
new variable. To handle it, the assembler (i) adds the entry <xxx, value> to
the symbol table, where value is the next available address in the RAM
space designated for variables, and (ii) completes the instruction’s
translation, using this address. In the Hack platform, the RAM space
designated for storing variables starts at 16 and is incremented by 1 after
each time a new variable is found in the code.


