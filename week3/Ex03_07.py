#-*-coding:UTF-8 -*-
#  EX03_07.py
#
#  使用 yield 模擬 range() 
#  

def myrange(n):
    x = 0
    while True:
        yield x
        x += 1
        if x == n:
            break 
            
print(list(myrange(10)))
