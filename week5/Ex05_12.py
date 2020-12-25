class A:
  pass
 
class B(A):
  pass

print(isinstance(5, int))   # returns True
print(isinstance(5, str))   # returns False

print(isinstance(A(), A))    # returns True

print(type(A()) == A    )    # returns True
print(isinstance(B(), A))    # returns True

print(type(B()) == A    )    # returns False

print(issubclass(A, A))    # returns True
print(issubclass(B, A))    # returns True
print(issubclass(A, B))    # returns False
