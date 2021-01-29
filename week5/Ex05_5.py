# 汽車類別
class Cars:
    door = 4  # 類別屬性
    name = 'Farrair'
    # 類別方法(Class Method)
    def __init__(self, brand):
      self.brand = brand
      pass

    @classmethod
    def open_door(cls, car):
        print(f"{cls.name} has {cls.door} doors. brand name is {car.brand}")
    
    
    
mazda = Cars("Mazda")
mazda.open_door(mazda)  #透過物件呼叫
# Cars.open_door()  #透過類別呼叫