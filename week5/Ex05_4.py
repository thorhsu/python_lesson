# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    # 實體方法(Instance Method)
    def drive(self):
        print(f"your {self.color} {self.brand} is driving.")
        self.message()  # 呼叫instance中的其他方法
    # 實體方法(Instance Method)
    def message(self):
        print("Message method is called.")
mazda = Cars("blue", "Mazda")
mazda.drive()
