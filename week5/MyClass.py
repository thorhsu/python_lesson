class MyClass:
  classAttr = 4 #class attribute
  def __init__(self, attr1, attr2):
    self.attr1 = attr1 #instance attribute
    self.attr2 = attr2

myClass = MyClass("Thor", 53)
print(id(myClass))
myClass1 = MyClass("Allie", 15)

print(myClass.attr1, myClass.attr2, myClass.classAttr)
MyClass.classAttr = 5
print(myClass1.attr1, myClass1.attr2, myClass1.classAttr)
print(MyClass.classAttr)