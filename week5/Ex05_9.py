# 交通工具(基底類別)
class Vehicle:
    # 建構式
    def __init__(self, color, drive_way):
        self.color = color  #顏色屬性
        self.drive_way = drive_way  #顏色屬性
    # 駕駛方法
    def drive(self):
        print(f"I am {self.drive_way}.")

# 汽車子類別
class Car(Vehicle):
    # 加速方法
    def accelerate(self):
        print("accelerate is method called.")

# 飛機子類別
class Airplane(Vehicle):
    # 飛行方法
    def fly(self):
        print("fly method is called.")

car = Car("red", "driving")
car.drive()

plane = Airplane("white", "flying")
plane.drive()
