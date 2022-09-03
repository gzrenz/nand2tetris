from VMI import VirtualMachine
from Parser import Parser 
from CodeWriter import CodeWriter 

import unittest 

class testRandom(unittest.TestCase): 
    """Testing functions or definitions"""

    # Tests codewriter add function 
    def testAdd(self): 
        coder = CodeWriter(open('data/testAdd.txt', 'w')) 
        coder.writeArithmetic(command="add")
        return 

class testSimpleAdd(unittest.TestCase): 
    """Testing the convertion of SimpleAdd.vm to SimpleAdd.asm"""

    def test(self): 
        vm = VirtualMachine('data/StackArithmetic/SimpleAdd/SimpleAdd.vm')
        testContent = open('data/StackArithmetic/SimpleAdd/SimpleAddTest.asm').read() 
        output = open('data/StackArithmetic/SimpleAdd/SimpleAdd.asm').read() 
        self.assertAlmostEqual(output, testContent) 
        return 

if __name__ == "__main__": 
    unittest.main() 