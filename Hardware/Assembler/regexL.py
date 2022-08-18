import re 

labelPattern = re.compile(r'\((\w)+\)|\((\w)+.(\w)+\)')
test1 = '(ball.dispose)'
test2 = '(ball.create)' 

if labelPattern.search(test1): 
    print(labelPattern.search(test1).group())
    print(re.search('\w+.\w+|(\w+)|(\d+)', test1).group()) 
else: 
    print('failed')
