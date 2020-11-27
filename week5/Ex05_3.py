class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge



class Guy:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    def __repr__(self):
      return "the repr"
    def __str__(self):
      return "the str"
p = Person('Pankaj', 34)
print(repr(p))
print(str(p))
p = Guy('Pankaj', 34)
print(repr(p))
print(str(p))