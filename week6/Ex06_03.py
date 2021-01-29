#-*-coding:UTF-8 -*-
#  EX07_02.py
#  
#  自訂例外範例
#  
#  錢包總金額為1000元，如果購買商品總金額超過1000
#  將會引發一個金額不足的例外


shoppingcart = {'fruits':400,'shoes':700 }

class InsufficientError(Exception): 
  pass
  # def __init__(self, insufficient_money): 
  #     print("Instance Created")
  #     super().__init__(insufficient_money)
  #     self.insufficient_money = insufficient_money

def buy(items):
    cash = 1000
    total = 0
    try:
        for price in items.values():
            total += price
        if total > cash:
            raise InsufficientError(total - cash)
    except InsufficientError as e:
        print('INSUFFICIENT FUND', e.insufficient_money)

buy(shoppingcart)
