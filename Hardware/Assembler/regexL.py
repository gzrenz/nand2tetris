import re 

labelPattern = re.compile(r'\(\w+\W\w+\W\w+\)|\(\w+.\w+\)|\((\w)+\)')
labelPattern1 = re.compile(r'\(\w+\)')
test1 = '(memory.alloc)'
test2 = '@memory.alloc' 
test3 = '(ball.move$if_true0)'

if labelPattern.search(test1): 
    print(labelPattern.search(test3).group())
    print(re.search('\w+\W\w+\W\w+|\w+.\w+|\w+|\d+', test3).group()) 
else: 
    print('failed')
