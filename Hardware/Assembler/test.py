from ParserC import Parser 

parser = Parser(open('data/pong/Pong.asm')) 
parser.currentline = '(ball.dispose)' 
print(parser.instructionType()) 
parser.currentline = '(@asldkjfs)' 
print(parser.instructionType()) 

