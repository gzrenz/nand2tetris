import unittest
from ParserC import Parser
import re  

class ParserTestCase(unittest.TestCase): 
    """Test parser functions"""

    file = open('data/add/Add.asm') 
    parser = object

    def test_init(self): 
        self.parser = Parser(self.file) 
        testLines = ['@2', 'D=A', '@3', 'D=D+A', '@0', 'M=D']
        self.assertEqual(self.parser.lines, testLines)

    def test_program_traversal(self): 
        parser = Parser(open('data/max/Max.asm'))
        # print(f"\nParsed lines: {parser.lines}")
        while True: 
            if not parser.hasMoreLines(): 
                break 
            parser.advance() 
        parser.file.close() 
    
    def test_instruction_type_and_symbol(self): 
        parser = Parser(open('data/max/Max.asm'))
        extracted = []
        while True: 
            if not parser.hasMoreLines(): 
                break 
            parser.advance()  
            if parser.instructionType == 'L_INSTRUCTION': 
                extracted.append(parser.symbol())
        self.assertIn('OUTPUT_FIRST', extracted)
        self.assertIn('OUTPUT_D', extracted)
        self.assertIn('INFINITE_LOOP', extracted)
        print(f"Extracted: {extracted}")
        parser.file.close() 

    def test_random(self): 
        parser = Parser(open('data/max/Max.asm')) 
        print(parser.lines)

    # def test_symbol(self): 
    #     parser = Parser(open('data/max/Max.asm')) 
    #     extracted = []
    #     while True: 
    #         if not parser.hasMoreLines(): 
    #             break 
    #         parser.advance() 
    #         parser.instructionType() 
    #         if parser.instType == 'L_INSTRUCTION': 
    #             extracted.append(parser.symbol)
    #             print('hello')
    #         self.assertIn('OUTPUT_FIRST', extracted)



    def test_terminate(self): 
        self.file.close() 

    def test_removeEmpty(self): 
        return 


if __name__  == '__main__': 
    unittest.main() 


# file = open('data/add/Add.asm', 'r')
# lines = file.readlines() 
# for i, line in enumerate(lines): 
#     line += 'A '
#     lines[i] = line  
# print(lines)


# strings = ['A                ', 'A         ', 'A\n', 'A\t']
# print(string.replace(' ', ''))