class Plus1:
  def add(self, x):
    y = x + 1
    return y

class Plus2(Plus1):
  def add(self, x):
    y = super().add(x)
    return y + 1

class Plus3(Plus2):
  def add(self, x):
    y = super(Plus3, self).add(x)
    return y + 1

plus2 = Plus2()
print(plus2.add(2) )

plus3 = Plus3()
print(plus3.add(2) )