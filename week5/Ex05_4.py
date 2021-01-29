# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    # 實體方法(Instance Method)
    def drive(self, kph):
        print(f"your {self.color} {self.brand} is driving.")
        self.kph = kph
        self.message()  # 呼叫instance中的其他方法
    # 實體方法(Instance Method)
    def message(self):
        print(f"Instance method is called. The current kph is {self.kph}")
mazda = Cars("blue", "Mazda")
mazda.drive(100)
toyota = Cars("silver", "Toyota")
toyota.drive(60)
