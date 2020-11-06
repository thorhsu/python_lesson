def foo():
    print("start...")
    while True:
      yield 10

def boo(n):    
    x = 0
    while True:
        yield x
        x += 1
        if x == n:
            break

g = foo()

print(next(g))
print("*"*20)
print(next(g))
for i in boo(3):
  print(i)
print(next(g))
