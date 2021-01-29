print(123, 234)
print(123, 234, sep="_")
print(123, 234, sep=",", end='\n___')
# append
fileout = open('./filetest.txt' , 'a')
# write
# fileout = open('./filetest.txt' , 'w')
print(123, 234, sep="_", end='\r\n___\r\n', file=fileout)