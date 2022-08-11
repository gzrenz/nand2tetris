from cgi import test
import unittest
from HackAssembler import Assembler

class HackAssemblerTestCase(unittest.TestCase): 
    """Tests for the Hack Assembler with input data/add/Add.asm."""

    def test_assembler_filereader(self):
        testDir = 'data/add/Add.asm'
        assembler = Assembler(testDir) 
        testContent = ''
        with open(testDir, 'r') as f: 
            testContent = f.read() 
        content = assembler.file.read() 
        self.assertEqual(content, testContent)
        return 
        

    def test_assembler_symbolDict(self): 
        assembler = Assembler('data/add/Add.asm') 
        symbolDict = {
            'R0' : 0, 
            'R1' : 1, 
            'R2' : 2, 
            'R3' : 3, 
            'R4' : 4, 
            'R5' : 5, 
            'R6' : 6, 
            'R7' : 7, 
            'R8' : 8, 
            'R9' : 9, 
            'R10': 10, 
            'R11': 11, 
            'R12': 12, 
            'R13': 13, 
            'R14': 14, 
            'R15': 15, 
            'SP' : 0, 
            'LCL' : 1, 
            'ARG' : 2, 
            'THIS' : 3, 
            'THAT' : 4, 
            'SCREEN' : 16384, 
            'KBD' : 24576
        }
        self.assertEqual(symbolDict, assembler.symbolDict)

    def test_assembler_writer(self): 
        testDir = 'data/add/Add.asm' 
        assembler = Assembler(testDir) 
        assembler.writer.write('Hello\nworld')
        assembler.writer.close() 
        text = '' 
        with open('data/add/Add.hack', 'r') as r: 
            text= r.read() 
        textTest = 'Hello\nworld'
        self.assertEqual(text, textTest)



class HackAssemblerTestCase1(unittest.TestCase): 
    assembler = Assembler('data/add/Add.asm')

    def test_addEntry(self):    
        self.assembler.addEntry('LABEL', 0)
        self.assembler.addEntry('variable', 16) 
        self.assertEqual(self.assembler.symbolDict['LABEL'], 0)
        self.assertEqual(self.assembler.symbolDict['variable'], 16)

    def test_contains(self): 
        self.assertTrue(self.assembler.contains('LABEL'))
        self.assertTrue(self.assembler.contains('variable'))

    def test_getAddress(self): 
        LABELAddr = self.assembler.getAddress('LABEL')
        variableAddr = self.assembler.getAddress('variable')

        self.assertEqual(LABELAddr, 0)
        self.assertEqual(variableAddr, 16)

    def test_close(self): 
        self.assembler.file.close() 
        self.assembler.writer.close() 

class HackAssemblerTestFirstPass(unittest.TestCase): 
    """Tests the first pass method in assembler using file max.asm"""

    assembler = Assembler('data/max/Max.asm')

    def test_symbolTable(self): 
        self.assembler.firstPass() 
        self.assertTrue(self.assembler.contains('OUTPUT_FIRST'))
        self.assertTrue(self.assembler.contains('OUTPUT_D'))
        self.assertTrue(self.assembler.contains('INFINITE_LOOP'))
        self.assertEqual(self.assembler.getAddress('OUTPUT_FIRST'), 10)
        self.assertEqual(self.assembler.getAddress('OUTPUT_D'), 12)
        self.assertEqual(self.assembler.getAddress('INFINITE_LOOP'), 14)

    # def testClose(self): 
    #     self.assembler.file.close() 
    #     self.assembler.writer.close() 

if __name__ == '__main__': 
    unittest.main()     