import unittest 

from ParserC import Parser 

class TestCaseParserPong(unittest.TestCase): 
    """Testing the parser for Pong asm file and making sure labels correspond to the right value"""

    parser = Parser(open('data/pong/Pong.asm')) 

    def test_initialTest(self): 
        print(self.parser.lines)
        open('data/pongLines.txt', 'w').write(f"{self.parser.lines}")


if __name__ == '__main__': 
    unittest.main() 