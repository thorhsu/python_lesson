
def test1(a, b=2, c=3):
  print(a,b,c)
  return a, b

var1, var2 = test1(1, )
print(var1, var2)