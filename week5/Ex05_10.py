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
  def __init__(self, color, drive_way, wheel_number, door_number, power):
    self.wheel_number = wheel_number
    self.door_number = door_number
    self.power = power
    super(Car, self).__init__(color, drive_way)

  # 加速方法
  def accelerate(self):
      print("accelerate method is called.")

# 飛機子類別
class Airplane(Vehicle):
  # 飛行方法
  def fly(self):
      print("fly method is called.")

class ElectricCar(Car):
  def __init__(self, color, drive_way, wheel_number, door_number, power, brand):
    super(ElectricCar, self).__init__(color, drive_way, wheel_number, door_number, power)
    self.brand = brand

  def accelerate(self):
    print(f"{self.brand} 0~100 km/hr acceleration: 4 seconds.")


car = Car("red", "driving", 4, 2, 100)
car.drive()
car.accelerate()

eCar = ElectricCar("white", "Robot auto-driving", 3, 2, 50, "ECar")
eCar.drive()
eCar.accelerate()

plane = Airplane("white", "flying")
plane.drive()


