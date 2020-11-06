# num = int(input('Please input a number:'))

# total = 0
# for i in range(num + 1):
#   total = total + i
#   # total += i
# print(total)
def sum(num):
  total = 0
  for i in range(num + 1):
    # total = total + i
    total += i
  return total, i


number = int(input('Please input a number:'))
total, i = sum(number)
print(total, i)


