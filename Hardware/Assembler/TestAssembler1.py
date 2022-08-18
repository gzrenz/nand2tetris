import unittest 
from HackAssembler import Assembler
# Test programs 

    # No Symbolic References 
# class HackAssemblerTestAdd(unittest.TestCase): 
#     assembler = Assembler('data/add/Add.asm')
#     compareFile = open('data/add/AddTest.hack') 

#     resultFile = open('data/add/Add.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

# class HackAssemblerTestMax(unittest.TestCase):
#     assembler = Assembler('data/max/Max.asm') 
#     compareFile = open('data/max/MaxTest.hack')  

#     resultFile = open('data/max/Max.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

# class HackAssemblerTestRect(unittest.TestCase):
#     assembler = Assembler('data/rect/Rect.asm') 
#     compareFile = open('data/rect/RectTest.hack')  

#     resultFile = open('data/rect/Rect.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

class HackAssemblerTestPong(unittest.TestCase): 
    assembler = Assembler('data/pong/Pong.asm')
    compareFile = open('data/pong/PongTest.hack') 

    resultFile = open('data/pong/Pong.hack') 

    compareContent = compareFile.read() 
    resultContent = resultFile.read() 

    print(assembler.symbolDict) 

    def test_compare(self):
        self.assertEqual(self.resultContent, self.compareContent)  


    # With Symbolic References 
# class HackAssemblerTestMaxL(unittest.TestCase): 
#     assembler = Assembler('data/max/MaxL.asm')
#     compareFile = open('data/max/MaxLTest.hack')  

#     resultFile = open('data/add/Add.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

# class HackAssemblerTestRectL(unittest.TestCase): 
#     assembler = Assembler('data/rect/RectL.asm')
#     compareFile = open('data/rect/RectLTest.hack')  

#     resultFile = open('data/add/Add.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

# class HackAssemblerTestPongL(unittest.TestCase): 
#     assembler = Assembler('data/pong/PongL.asm')
#     compareFile = open('data/pong/PongLTest.hack')  

#     resultFile = open('data/add/Add.hack') 

#     compareContent = compareFile.read() 
#     resultContent = resultFile.read() 

#     def test_compare(self):
#         self.assertEqual(self.resultContent, self.compareContent) 

if __name__ == '__main__': 
    unittest.main()     