import re 
# from Parser import Parser 

# parser = Parser('data/add/Add.asm')
# while True: 
#     if parser.hasMoreLines(): 
#         parser.advance() 
#         print(parser.currentline) 
#     else: 
#         print('file is empty') 
#         break 

# labelPattern = re.compile(r'\((\w)*\)')
# mo = labelPattern.search('(HAKDOG)')
# print(mo.group()) 
# mo = labelPattern.search('(14)')
# print(mo.group()) 

# addressPattern = re.compile(r'@(\w)*|@(\d)*')
# mo = addressPattern.search('a;sdlfkjs @var') 
# print(mo.group()) 
# mo = addressPattern.search('a;sdlfkjs @14') 
# print(mo.group()) 

# compPattern = re.compile(r'0|1|D|M')
# mo = compPattern.search('asd;fjasd;lfkj M 1 0') 
# print(mo.group()) 

dict = {} 
dict['hello'] = 'world' 
print(dict['hello'])

