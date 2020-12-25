class A3:
  def __init__(self):
    self.a = "A3"
  
  def print_a(self):
    print(self.a)

class B3:
  def __init__(self):
    self.b = "B3"
  
  def print_b(self):
    print(self.b)

class C3:
  def __init__(self):
    self.c = "C3"
  
  def print_c(self):
    print(self.c)

class D3(A3, B3, C3):
  '''之所以要這麼做，這是因為依序呼叫每個父類別的 __init__() 才能有效繼承每個父類別的實體屬性，
  不然子類別只會繼承其中一個父類別的 __init__() ，對於其他跟父類別同名稱的方法亦同，
  若是需要先實作父類別同名稱的方法，就要用 super() 先呼叫一次。'''
  def __init__(self):
    super().__init__()
    super(A3, self).__init__()
    super(B3, self).__init__()
    super(C3, self).__init__()

d = D3()
d.print_a()
d.print_b()
d.print_c()