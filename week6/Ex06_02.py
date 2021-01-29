try:
  raise IndexError('11')
except IndexError as e:
  print(type(e), str(e))