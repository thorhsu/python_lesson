#-*-coding:UTF-8 -*-
#範例程式 EX02_03.py
#輸入兩個數字比大小
num1 = int(input('Please input a num1:'))
num2 = int(input('Please input a num2:'))
if num1 == num2:
  print(num1,'equals',num2)
elif num1 < num2:
  print(num1, 'less than',num2)
else:
  print(num1, 'greater than',num2)