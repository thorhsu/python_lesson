class A2:
  a = "A2"
  
  @classmethod
  def print_a(cls):
    print(cls.a)
  
  @classmethod
  def print(cls):
    print(cls.a)

class B2:
  b = "B2"
  
  @classmethod
  def print_b(cls):
    print(cls.b)
  @classmethod
  def print(cls):
    print(cls.b)

class C2:
  c = "C2"
  
  @classmethod
  def print_c(cls):
    print(cls.c)
  @classmethod
  def print(cls):
    print(cls.c)

class D2(A2, B2, C2):
  pass

D2.print_a()
D2.print_b()
D2.print_c()
D2.print()  # 以最左邊的優先
