import sys 

dir = str(sys.argv[1]) 
writer = open(dir, 'w')
writer.write('Hello\nworld')
